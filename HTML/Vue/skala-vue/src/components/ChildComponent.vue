<template>
    <h1>이름 {{ name }}, 성별: {{ gender }}</h1>
    <h1>자산: {{ assets.join() }}</h1>
    <label><input v-model="money"></input></label><button @click="send">전달</button>
    <h2>부모님의 잔소리: {{ nagMessage }}</h2>
</template>

<script setup>
import { ref } from "vue";

const props = defineProps({
    name: String,
    gender: String,
    assets: Array
});

const money = ref(0);

const emit = defineEmits(['send']);
const send = () => {
    emit('send', Number(money.value));
};

const nagMessage = ref('');
function nag(msg) {
    nagMessage.value = msg;
}

defineExpose({
    nag
});
</script>