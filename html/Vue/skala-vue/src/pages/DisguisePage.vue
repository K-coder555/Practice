<template>
<div>
<h1>둔갑술 시전!</h1>
<p>홍길동이 <strong>{{ target }}</strong>으로 변신했습니다~</p>
</div>
</template>
<script setup>
import { useRoute, useRouter } from 'vue-router'
import { onMounted, ref } from 'vue'
const route = useRoute()
const router = useRouter()
const target = ref('???')
onMounted(() => {
if (route.query.target) {
 target.value = route.query.target
 router.replace({path: route.path, query: {}})
 // URL query 
}
 })
</script>

<!-- <template>
    <div class="card">
        <div class="card-body text-center">
            <div v-if="target">
                <h2>둔갑 완료!</h2>
                <p class="fs-4">당신은 <strong>{{ target }}</strong> (으)로 둔갑했습니다.</p>
                <div class="display-1">{{ emoji }}</div>
            </div>
            <div v-else>
                <p>메뉴에서 둔갑할 대상을 선택해주세요.</p>
            </div>
        </div>
    </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
    target: String
});

const emojiMap = {
    '호랑이': '🐯',
    '곰': '🐻',
    '여우': '🦊',
    '너구리': '🦝'
};

const emoji = computed(() => emojiMap[props.target] || '❓');

</script>

<style scoped>
.display-1 {
    font-size: 6rem;
}
</style> -->
