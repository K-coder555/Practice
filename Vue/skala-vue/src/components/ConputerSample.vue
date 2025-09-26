<template>
  <div>
    <input v-model="keyword" placeholder="카테고리를 입력하세요(과일,채소)" />
    <ul>
      <li v-for="item in filteredItems" :key="item.name">
        {{ item.name }} ({{ item.category }})
      </li>
    </ul>
  </div>
  <div> 개수: {{ result }}</div>
</template>
<script setup>
import { ref, reactive, computed, watch } from 'vue'

const keyword = reactive({
    category: '',
    name: ''
})


const items = reactive([
  { name: '사과', category: '과일' },
  { name: '바나나', category: '과일' },
  { name: '당근', category: '채소' },
  { name: '오이', category: '채소' },
  { name: '파인애플', category: '과일' }
])

const filteredItems = ref([])
watch(() => keyword.category, (newValue, oldValue)=>{
    filteredItems.value = items.filter(item => item.category == newValue)
}, {immediate : true})
//console.log(newValue, oldValue)
//const filteredItems = computed(() => items.filter(item => item.category == keyword.value))


const result = computed(() => keyword.value + `(${filteredItems.value.length})`)
</script>