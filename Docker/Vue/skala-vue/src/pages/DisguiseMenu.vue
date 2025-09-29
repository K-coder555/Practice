<template>
<div>
    <h1>둔갑술 선택 메뉴</h1>
    <button @click="goToDisguise('호랑이')">호랑이로 둔갑하기</button>
    <button @click="goToDisguise('도깨비')">도깨비로 둔갑하기</button>
</div>
</template>
<script setup>
 import { useRouter } from 'vue-router'
 const router = useRouter()
 function goToDisguise(target) {
 // “/disguise?target='호랑이' 형태로 경로 전환
 router.push({ path: '/disguise', query: { target } })
 }
 </script>

<!-- <template>
    <div class="list-group">
        <h4 class="mb-3">둔갑술 메뉴</h4>
        <router-link 
            v-for="target in disguiseTargets" 
            :key="target"
            :to="{ name: 'disguise', params: { target: target } }"
            class="list-group-item list-group-item-action"
        >
            {{ target }}로 둔갑하기
        </router-link>
    </div>
</template>

<script setup>
import { ref } from 'vue';

const disguiseTargets = ref([
    '호랑이',
    '곰',
    '여우',
    '너구리'
]);
</script>

<style scoped>
.list-group-item.router-link-active {
    background-color: #0d6efd;
    color: white;
    border-color: #0d6efd;
}
</style> -->
