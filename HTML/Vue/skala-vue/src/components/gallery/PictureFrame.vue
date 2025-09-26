<template>
<slot></slot>
<h1>액자 ID: {{ FrameId }}</h1>
    <slot name="content"></slot>
    
    <slot name="author"></slot>
</template>

<script setup>
    const props = defineProps({
        FrameId: String,
        
    })
</script>