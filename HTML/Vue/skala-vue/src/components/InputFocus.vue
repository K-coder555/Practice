 <template>
 <div>
 <button @click="showInputBox">입력창 열기</button>
 <div v-if= "isVisible">
    <input ref="inputRef" placeholder="이름입력" />
 </div>
 </div>
 </template>
 <script setup>
    import { ref, nextTick } from 'vue'
    
    const isVisible = ref(false)
    const inputRef = ref(null)

    async function showInputBox() {
    isVisible.value = true
    await nextTick()
    inputRef.value.focus()
    }
    
 </script>
