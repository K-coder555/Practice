<template>
    <div>
      <h2>기술연습</h2>
      <button @click="walking">걷기(-1kg)</button><button @click="running">달리기(-2kg)</button>
    </div>
</template>

<script setup>
import { defineEmits } from 'vue';

const emit = defineEmits(['train']);

const walking = () => {
  emit('train', 1);
};

const running = () => {
  emit('train', 2);
};
</script>