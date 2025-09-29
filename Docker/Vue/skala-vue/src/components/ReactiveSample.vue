<template>
 <div>
 <p>이름 : <input v-model="user.name" /></p>
 <p>나이 : {{ user.age }} <button @click="user.age++">한 살 더</button></p>
 <p>과일목록 : {{ fruits.join(', ') }}</p>
 <button @click="fruits.push('귤')">과일추가</button>
 <div>{{readonlyUser.age}}</div>
 </div>
</template> 
 
<script setup>
   import { reactive, readonly } from 'vue'
   const user = reactive({ name: '홍길동', age: 20 })
   const readonlyUser = readonly(user)
   const fruits = reactive(['사과', '배'])
</script>