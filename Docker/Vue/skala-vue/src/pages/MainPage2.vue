
<template>
    <div class="container mt-5">
        <div class="row">
            <div class="col-md-4">
                <DisguiseMenu />
            </div>
            <div class="col-md-8">
                <router-view></router-view>
            </div>
        </div>
    </div>
</template>

<script setup>
import DisguiseMenu from './DisguiseMenu.vue';
</script>
