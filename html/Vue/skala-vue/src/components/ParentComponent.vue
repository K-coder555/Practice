<template>
    <h1>자식이 준 용돈: {{money}}</h1>
    <ChildComponent ref="child1" :name="children[0].name" :gender="children[0].gender" :assets="children[0].assets" 
    @send="addmoney"></ChildComponent>
    <!-- <ChildComponent ref="child2" :name="children[1].name" :gender="children[1].gender" :assets="children[1].assets"
    @send="addmoney"></ChildComponent> -->
    <label>메시지: <input v-model="message"></input></label><button @click="nagChildren">잔소리</button>
</template>

<script setup>
import { ref } from 'vue';
import ChildComponent from './ChildComponent.vue';
const children = [
    {name: "홍길동", gender: "남", assets: ["창","칼"]},
    {name: "아이유", gender: "여", assets: ["돈","집"]}
]
const money = ref(0);

function addmoney(childMoney) {
    money.value += childMoney;
}

const child1 = ref(null);
const child2 = ref(null);
const message = ref("");

function nagChildren() {
    // Optional Chaining (?.) to prevent errors if a child component is not yet mounted.
    child1.value?.nag(message.value);
    child2.value?.nag(message.value);
}
</script>