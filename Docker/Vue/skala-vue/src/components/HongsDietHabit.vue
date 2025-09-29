<template>
    <h1>{{ title }}</h1>
    <div>
        <button v-for="habit in habits" @click="doHabit(habit.weight)">{{habit.name}}
            ({{habit.weight}}) </button>
    </div>
</template>

<script setup>
    const props = defineProps({
        title: {
            type: String,
            habits: Array // name, weight
        }
    })
const emit = defineEmits(['weightChanged'])

function doHabit(w) {
    console.log(w)
    emit('weightChanged', w)
}
</script>