<template>
    <div class="m-2">

        <template v-for="(option, index) in options" :key="index">
            <input 
                type="radio" 
                class="form-check-input"
                :name="name"
                :id="`${name}-${option.value}`"
                :value="option.value"
                :checked="option.value === modelValue"
                :disabled="disabled"
                @change="onChange(option)"
                autocomplete="off"
            >
            <label class="btn btn-outline-primary" :for="`${name}-${option.value}`">{{ option.label }}</label>
        </template>
    </div>
</template>

<script setup>
import { computed } from 'vue';

// Predefined option sets
const predefinedOptions = {
    gender: [
        { label: "남", value: "m" },
        { label: "여", value: "f" },
    ],
    school: [
        { label: "초등학교", value: "01" },
        { label: "중학교", value: "02" },
        { label: "고등학교", value: "03" },
        { label: "대학교", value: "04" },
    ]
};

// Props: name(그룹명), options(라디오 옵션 목록), modelValue(선택된 값), disabled(비활성화 여부)
const props = defineProps({
    name: {
        type: String,
        required: true
    },
    options: {
        type: Array,
        default: null,
        validator: (value) => {
            if (!value) return true; // Allow null
            // 각 옵션이 label과 value 속성을 가지고 있는지 확인
            return value.every(option => 'label' in option && 'value' in option);
        }
    },
    optionSet: {
        type: String,
        default: null
    },
    modelValue: [String, Number, Boolean],
    disabled: {
        type: Boolean,
        default: false
    }
});

//Computed: options(라디오 옵션 목록)

const options = computed(() => {
    if (props.options) {
        return props.options;
    }
    if (props.optionSet && predefinedOptions[props.optionSet]) {
        return predefinedOptions[props.optionSet];
    }
    return [];
});

// Emits: update:modelValue(v-model 지원), changed(선택된 항목 정보 전달)
const emit = defineEmits(['update:modelValue', 'changed'])

// 라디오 버튼 변경 시 호출되는 함수
function onChange(option) {
    // v-model 업데이트
    emit('update:modelValue', option.value);
    // changed 이벤트 발생
    emit('changed', option);
}
</script>

<style scoped>
/* Optional: Add custom styles here if needed */
</style>