<template>
    <div class="mb-3">
        <label :for="inputId" class="form-label" :class="getSize">{{ label }}</label>
        <input
            v-model="inputValue"
            :id="inputId"
            :type="type"
            :class="getSize"
            :placeholder="placeholder"
            :size="size"
            :disabled="disabled"
            :readonly="readonly"
            :value="modelValue"
            @input="$emit('update:modelValue', $event.target.value)"
            @key-up.enter ="$emit('enterKey')"
        >
        <input
            v-model="inputValue2"
            :id="inputId"
            :type="type"
            :class="getSize"
            :placeholder="placeholder"
            :size="size"
            :disabled="disabled"
            :readonly="readonly"
            :value="modelValue"
            @input="$emit('update:modelValue', $event.target.value)"
            @key-up.enter ="$emit('enterKey')"
        >
    </div>
</template>

<script setup>
    import { computed } from 'vue';
    const inputValue = defineModel('email');
    const inputValue2 = defineModel('id');

    const props = defineProps({
        label: String,
        type: {
            type: String,
            default: 'text'
        },
        id: String,
        placeholder: String,
        size: String,
        disabled: Boolean,
        readonly: Boolean,
        modelValue: [String, Number],
        inputValue: String
    })


    function getSize() {
        if(props.size == 'sm'){
            return 'form-control-sm'
        }else if(props.size == 'lg'){
            return 'form-control-lg'
        }else{
            return 'form-control'
        }
    }

    defineEmits(['update:modelValue'])

    const inputId = computed(() => props.inputValue || `input-${props.label.toLowerCase().replace(/\s+/g, '-')}`);
</script>

<style scoped>

</style>