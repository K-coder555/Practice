import os
import psycopg2
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores.pgvector import PGVector
from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import SQLDatabaseLoader
from langchain_community.utilities import SQLDatabase
from langchain.retrievers import ContextualCompressionRetriever
from langchain_community.document_transformers import LongContextReorder

load_dotenv()

# --- 공통 LLM + Embedding ---
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
embedding = OpenAIEmbeddings(model="text-embedding-ada-002")

# --- DB 접속정보 ---
CONNECTION_STRING = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

# --- Vector Retriever ---
vectorstore = PGVector(
    connection_string=CONNECTION_STRING,
    embedding_function=embedding,
    collection_name="cases",     # law.cases 매핑됨
)
vector_retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k":5})

# --- BM25 Retriever ---
# documents 전체를 불러오는 과정 필요 (ex: 초기화 시 한 번만 실행)
db = SQLDatabase.from_uri(CONNECTION_STRING, include_tables=["cases"], schema="law")

QUERY = """
SELECT content, case_no, case_title, court, decided_at
FROM law.cases
"""

# row는 dict로 들어옵니다.
def page_content_mapper(row):
    return row.get("content", "")

def metadata_mapper(row):
    return {
        "case_no": row.get("case_no"),
        "case_title": row.get("case_title"),
        "court": row.get("court"),
        "decided_at": row.get("decided_at"),
    }

loader = SQLDatabaseLoader(
    QUERY,
    db,
    page_content_mapper=page_content_mapper,
    metadata_mapper=metadata_mapper,
    source_columns=["case_no"]  # 선택: 메타데이터 source에 case_no 표시
)

docs = loader.load()

bm25_retriever = BM25Retriever.from_documents(docs)
bm25_retriever.k = 5

# --- Ensemble Retriever ---
ensemble_retriever = EnsembleRetriever(
    retrievers=[vector_retriever, bm25_retriever],
    weights=[0.6, 0.4]   # 임의 비율 (튜닝 가능)
)

# --- 공통 QA 체인 ---
PROMPT = ChatPromptTemplate.from_messages([
    ("system", "너는 저작권 판례 Q&A 어시스턴트다. 제공된 컨텍스트 내에서만 답하라."),
    ("human", "질문: {question}\n\n컨텍스트:\n{context}")
])

# --- Pre Retriever: HYDE - 가설 문서 생성 후 그걸로 검색 ---
HYDE_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "너는 저작권 판례 Q&A 어시스턴트다."),
    ("human", "아래 질문에 대한 '가설 문서'를 5~7문장으로 한국어로 작성하라. "
              "사실처럼 자연스럽게 서술하되, 출처·문헌 언급은 금지.\n\n질문: {question}")
])

def hyde_expand(question: str) -> str:
    msgs = HYDE_PROMPT.format_messages(question=question)
    print("===가상문서 생성 ===")
    return llm.invoke(msgs).content.strip()


# --- Post Retriever ---
RERANK_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "문서와 질문의 관련성을 0-10점으로 평가하라. 숫자만 응답."),
    ("human", "질문: {question}\n\n문서: {document}\n\n관련성 점수 (0-10):")
])

# --- Post Retriever 1: Document Filtering - 중복/저품질 문서 제거 ---
def filter_documents(docs, min_length=50, similarity_threshold=0.8):
    """중복 및 저품질 문서 필터링"""
    print("=== 문서 필터링 ===")
    filtered_docs = []
    
    for doc in docs:
        # 1. 길이 필터링
        if len(doc.page_content.strip()) < min_length:
            print(f"길이 부족으로 제외: {doc.page_content[:30]}...")
            continue
        
        # 2. 중복 필터링 (간단한 문자열 유사도)
        is_duplicate = False
        for existing_doc in filtered_docs:
            # 첫 100자 기준으로 중복 체크
            if doc.page_content[:100] == existing_doc.page_content[:100]:
                print(f"중복으로 제외: {doc.page_content[:30]}...")
                is_duplicate = True
                break
        
        if not is_duplicate:
            filtered_docs.append(doc)
            print(f"포함: {doc.page_content[:50]}...")
    
    return filtered_docs
#--- Post Retriever 2: Rerank - LLM 기반 관련성 재평가 
def rerank_documents(question: str, docs, top_k=5):
    #LLM을 사용해 문서를 재순위화
    print("=== 문서 재순위화 ===")
    scored_docs = []
    
    for doc in docs:
        msgs = RERANK_PROMPT.format_messages(question=question, document=doc.page_content[:500])
        try:
            score = float(llm.invoke(msgs).content.strip())
            scored_docs.append((doc, score))
            print(f"점수: {score:.1f} - {doc.page_content[:50]}...")
        except:
            scored_docs.append((doc, 0.0))  # 파싱 실패시 낮은 점수
    
    # 점수 기준 내림차순 정렬 후 top_k 반환
    scored_docs.sort(key=lambda x: x[1], reverse=True)
    return [doc for doc, score in scored_docs[:top_k]]

# PreRetriever + Retriever + PostRetriever Run chain
def run_chain_hyde_rerank(retriever, question: str):
    #Pre Retriever: HYDE / 질문 + 가설문서를 합쳐서 검색 신호 강화
    hypo = hyde_expand(question)
    tuned_query = f"{question}\n\n{hypo}"

    # Retriever: 초기 문서 검색 (더 많이 가져오기)
    docs = retriever.get_relevant_documents(tuned_query)
    print(f"초기 검색된 문서 수: {len(docs)}")
    
    # Post Retriever 1: Document Filtering
    filtered_docs = filter_documents(docs, min_length=30)
    
    # Post Retriever 2: Rerank
    reranked_docs = rerank_documents(question, filtered_docs, top_k=3)
    print(f"최종 선택된 문서 수: {len(reranked_docs)}")

    #최종 context 생성 및 답변
    context = "\n---\n".join([d.page_content[:300] for d in reranked_docs])
    msgs = PROMPT.format_messages(question=question, context=context)
    return llm.invoke(msgs).content


if __name__ == "__main__":
    q = "저작권 침해 손해배상액 산정 기준은?"
    print("=== VectorRetriever ===")
    print(run_chain_hyde_rerank(vector_retriever, q))
    print("=== BM25Retriever ===")
    print(run_chain_hyde_rerank(bm25_retriever, q))
    print("=== EnsembleRetriever ===")
    print(run_chain_hyde_rerank(ensemble_retriever, q))

#rerank 등 2가지 정도만 RAG 테크닉 적용해보기