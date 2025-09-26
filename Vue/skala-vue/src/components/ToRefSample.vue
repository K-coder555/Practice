 <script setup>
 import { ref, unref, reactive, toRef, toRefs } from 'vue'
 const state = reactive({
 name: '홍길동',
 age: 20
 })

const { name, age } = toRefs(state)
const count = ref(20)
const num = 30

console.log(count, num)
//  const name = toRef(state, 'name')
//  const age = toRef(state, 'age')
 </script>

 <template>
 <input v-model="name" />
 <input v-model="state.age" type="number" /> 
<div>{{ state.name }}, {{ state.age }}</div>
 </template>
