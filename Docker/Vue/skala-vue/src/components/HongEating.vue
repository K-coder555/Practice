<template>
    <div>
      <h2>음식먹기</h2>
      <button @click="eatBurger">햄버거(+1kg)</button><button @click="eatPizza">피자(+2kg)</button>
    </div>
</template>
<script setup>
import { defineEmits } from 'vue';

const emit = defineEmits(['eat']);

const eatBurger = () => {
  emit('eat', 1);
};

const eatPizza = () => {
  emit('eat', 2);
};
</script>