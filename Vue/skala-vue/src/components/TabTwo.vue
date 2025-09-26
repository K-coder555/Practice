<template>
 <div class="m-2">
 <h3>Tab Two</h3>
 <p>This is the second tab.</p>
 </div>
 </template>
 <script>
 export default {
 name: 'TabTwo'
 }
 </script>
 <script setup>
 import { onMounted, onActivated } from 'vue'
 onMounted(() =>{
 console.log('TabTwo Mounted')
 })

 onActivated(() =>{
 console.log('TabTwo Activated')
 })
 
 </script>
