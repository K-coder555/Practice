<template>
 <div class="m-4">
 <h3>Tab One</h3>
 <input v-model="text" placeholder="Input something" />
 <p>Input: {{ text }}</p>
 </div>
 </template>
 <script>
 export default {
 name: 'TabOne'
 }
 </script>
 <script setup>
 import { ref, onMounted, onActivated, onDeactivated } from 'vue'
 const text = ref('')

 onMounted(() =>{
 console.log('TabOne Mounted')
 })

 onActivated(() => {
 console.log('TabOne Activated')
 })
 
 onDeactivated(() => {
 console.log('TabOne Deactivated')
 })
 </script>