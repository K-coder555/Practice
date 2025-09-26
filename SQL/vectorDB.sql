PostgreSQL pgvector 실습용 쿼리문
테이블 생성
CREATE TABLE IF NOT EXISTS design_doc (
    id            BIGSERIAL PRIMARY KEY,
    title         TEXT NOT NULL,
    content       TEXT NOT NULL,
    embedding_vector VECTOR(384) NOT NULL       -- 검색용 pgvector 컬럼
);


=================================================================
1단계: 유사도 쿼리 기본 구조 (코사인 거리)
=================================================================

1-1. 코사인 거리를 이용한 유사도 검색
WITH query_params AS (
    SELECT ARRAY(SELECT random() FROM generate_series(1, 384))::vector AS query_vector
)
SELECT 
    d.id,
    d.title,
    d.content,
    d.embedding_vector <=> q.query_vector AS cosine_distance
FROM design_doc d, query_params q
ORDER BY cosine_distance ASC
LIMIT 5;

-- 1-2. 코사인 유사도로 변환하여 표시 (1 - cosine_distance)
WITH query_params AS (
    SELECT ARRAY(SELECT random() FROM generate_series(1, 384))::vector AS query_vector
)
SELECT 
    d.id,
    d.title,
    d.content,
    1 - (d.embedding_vector <=> q.query_vector) AS cosine_similarity
FROM design_doc d, query_params q
ORDER BY cosine_similarity
LIMIT 5;

-- =================================================================
-- 2단계: 성능비교 (인덱스 없이 실행계획)
-- =================================================================

2-1. 실행계획 확인 (EXPLAIN ANALYZE)
EXPLAIN ANALYZE
WITH query_params AS (
    SELECT ARRAY(SELECT random() FROM generate_series(1, 384))::vector AS query_vector
)
SELECT 
    d.id,
    d.title,
    d.embedding_vector <=> q.query_vector AS cosine_distance
FROM design_doc d, query_params q
ORDER BY cosine_distance
LIMIT 10;

-- 2-2. 검색 시간 측정용 쿼리
DO $$
DECLARE
    start_time timestamp;
    end_time timestamp;
    elapsed_time interval;
BEGIN
    start_time := clock_timestamp();
    
    PERFORM d.id, d.title, d.embedding_vector <=> q.query_vector AS cosine_distance
    FROM design_doc d, 
         (SELECT ARRAY(SELECT random() FROM generate_series(1, 384))::vector AS query_vector) q
    ORDER BY cosine_distance
    LIMIT 10;
    
    end_time := clock_timestamp();
    elapsed_time := end_time - start_time;
    
    RAISE NOTICE '실행 시간: %', elapsed_time;
END $$;

-- =================================================================
-- 3단계: IVFFlat 인덱스 생성 (코사인 거리 기준)
-- =================================================================

-- 3-1. 코사인 거리용 IVFFlat 인덱스 생성
CREATE INDEX design_doc_cosine_idx ON design_doc USING ivfflat (embedding_vector vector_cosine_ops) 
WITH (lists = 100);

-- 3-2. 인덱스 생성 확인
SELECT 
    schemaname,
    tablename,
    indexname,
    indexdef
FROM pg_indexes 
WHERE tablename = 'design_doc';

-- =================================================================
-- 4단계: 인덱스 적용 후 실행계획 확인
-- =================================================================

-- 4-1. 인덱스 적용 후 실행계획 비교
EXPLAIN ANALYZE
WITH query_params AS (
    SELECT ARRAY(SELECT random() FROM generate_series(1, 384))::vector AS query_vector
)
SELECT 
    d.id,
    d.title,
    d.embedding_vector <=> q.query_vector AS cosine_distance
FROM design_doc d, query_params q
ORDER BY cosine_distance
LIMIT 10;

-- 4-2. 인덱스 사용 강제 및 성능 비교
SET enable_seqscan = off;
EXPLAIN ANALYZE
SELECT 
    id,
    title,
    embedding_vector <=> :query_vector AS cosine_distance
FROM design_doc
ORDER BY embedding_vector <=> :query_vector
LIMIT 10;
SET enable_seqscan = on;

-- 4-2. 검색 시간 측정용 쿼리
DO $$
DECLARE
    start_time timestamp;
    end_time timestamp;
    elapsed_time interval;
BEGIN
    start_time := clock_timestamp();
    
    PERFORM d.id, d.title, d.embedding_vector <=> q.query_vector AS cosine_distance
    FROM design_doc d, 
         (SELECT ARRAY(SELECT random() FROM generate_series(1, 384))::vector AS query_vector) q
    ORDER BY cosine_distance
    LIMIT 10;
    
    end_time := clock_timestamp();
    elapsed_time := end_time - start_time;
    
    RAISE NOTICE '실행 시간: %', elapsed_time;
END $$;

-- =================================================================
-- 5단계: LIMIT값 증가 후 검색 시간 비교
-- =================================================================

5-1. 시간 측정을 위한 벤치마크 함수 생성
CREATE OR REPLACE FUNCTION benchmark_vector_search(limit_count integer)
RETURNS text AS $$
DECLARE
    start_time timestamp;
    end_time timestamp;
    elapsed_time interval;
    result_text text;
BEGIN
    start_time := clock_timestamp();
    
    PERFORM d.id, d.title
    FROM design_doc d, 
         (SELECT ARRAY(SELECT random() FROM generate_series(1, 384))::vector AS query_vector) q
    ORDER BY d.embedding_vector <=> q.query_vector
    LIMIT limit_count;
    
    end_time := clock_timestamp();
    elapsed_time := end_time - start_time;
    
    result_text := 'LIMIT ' || limit_count || ' 실행 시간: ' || elapsed_time;
    RETURN result_text;
END;
$$ LANGUAGE plpgsql;

5-2. 각 LIMIT 값별 성능 측정
SELECT benchmark_vector_search(10) AS benchmark_result;
SELECT benchmark_vector_search(50) AS benchmark_result;
SELECT benchmark_vector_search(50) AS benchmark_result;
SELECT benchmark_vector_search(500) AS benchmark_result;

-- =================================================================
-- 6단계: vector_l2_ops vs vector_cosine_ops 차이 실험
-- =================================================================

-- 6-1. L2 거리(유클리드 거리)용 인덱스 생성
CREATE INDEX design_doc_cosine_idx ON design_doc USING ivfflat (embedding_vector vector_cosine_ops) 
WITH (lists = 100);

CREATE INDEX design_doc_l2_idx ON design_doc USING ivfflat (embedding_vector vector_l2_ops) 
WITH (lists = 100);

-- 6-2. 코사인 거리 vs L2 거리 비교 쿼리
-- 코사인 거리 검색
WITH query_params AS (
    SELECT ARRAY(SELECT random() FROM generate_series(1, 384))::vector AS query_vector
)
SELECT 
    d.id,
    d.title,
    d.embedding_vector <=> q.query_vector AS cosine_distance,
    'cosine' AS distance_type
FROM design_doc d, query_params q
ORDER BY d.embedding_vector <=> q.query_vector
LIMIT 5;
-- L2 거리 검색  
WITH query_params AS (
    SELECT ARRAY(SELECT random() FROM generate_series(1, 384))::vector AS query_vector
)
SELECT 
    d.id,
    d.title,
    d.embedding_vector <-> q.query_vector AS l2_distance,
    'l2' AS distance_type
FROM design_doc d, query_params q
ORDER BY d.embedding_vector <-> q.query_vector
LIMIT 5;
-- 6-3. 두 거리 메트릭 동시 비교
WITH query_params AS (
    SELECT ARRAY(SELECT random() FROM generate_series(1, 384))::vector AS query_vector
)
SELECT 
    d.id,
    d.title,
    d.embedding_vector <=> q.query_vector AS cosine_distance,
    d.embedding_vector <-> q.query_vector AS l2_distance,
    d.embedding_vector <#> q.query_vector AS inner_product
FROM design_doc d, query_params q
ORDER BY d.embedding_vector <=> q.query_vector
LIMIT 10;

-- 6-4. 인덱스별 성능 비교 (코사인)
EXPLAIN ANALYZE
WITH query_params AS (
    SELECT ARRAY(SELECT random() FROM generate_series(1, 384))::vector AS query_vector
)
SELECT d.id, d.title 
FROM design_doc d, query_params q
ORDER BY d.embedding_vector <=> q.query_vector
LIMIT 10;

-- 6-5. 인덱스별 성능 비교 (L2)
EXPLAIN ANALYZE
WITH query_params AS (
    SELECT ARRAY(SELECT random() FROM generate_series(1, 384))::vector AS query_vector
)
SELECT d.id, d.title 
FROM design_doc d, query_params q
ORDER BY d.embedding_vector <-> q.query_vector
LIMIT 10;

=================================================================
추가: 유용한 모니터링 쿼리들
=================================================================

인덱스 크기 확인
SELECT 
    schemaname,
    tablename,
    indexname,
    pg_size_pretty(pg_relation_size(indexname::regclass)) AS index_size
FROM pg_indexes 
WHERE tablename = 'design_doc';

-- 테이블 통계 정보
SELECT 
    schemaname,
    tablename,
    n_tup_ins AS inserted_rows,
    n_tup_upd AS updated_rows,
    n_tup_del AS deleted_rows,
    n_live_tup AS live_rows
FROM pg_stat_user_tables 
WHERE tablename = 'design_doc';

-- 벡터 차원 확인
SELECT vector_dims(embedding_vector) AS dimensions
FROM design_doc
LIMIT 1;


벡터 정규화 함수 (필요한 경우)
UPDATE design_doc 
SET embedding_vector = embedding_vector / sqrt(
    (SELECT sum(power(unnest(embedding_vector::float[]), 2)))
);