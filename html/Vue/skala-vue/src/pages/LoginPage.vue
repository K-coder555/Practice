<template>
    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-md-6">
                <div class="card">
                    <div class="card-header">
                        <h3 class="text-center">Login</h3>
                    </div>
                    <div class="card-body">
                        <form @submit.prevent="handleLogin">
                            <div class="mb-3">
                                <label for="email" class="form-label">Email address</label>
                                <input type="email" class="form-control" id="email" v-model="email" required>
                            </div>
                            <div class="mb-3">
                                <label for="password" class="form-label">Password</label>
                                <input type="password" class="form-control" id="password" v-model="password" required>
                            </div>
                            <div class="d-grid gap-2">
                                <button type="submit" class="btn btn-primary">Login</button>
                                <button type="button" class="btn btn-secondary" @click="goToSignup">Sign Up</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import {useRouter} from "vue-router"

const email = ref('');
const password = ref('');

const handleLogin = () => {
    if (!email.value || !password.value) {
        alert('Please enter both email and password.');
        return;
    }
    console.log('Logging in with:', {
        email: email.value,
        password: password.value
    });
    // Here you would typically handle the login logic,
    // e.g., by calling an API.
    alert(`Login attempt with email: ${email.value}`);
};
const router = useRouter()
// function useRouter() {
//     router.push('/signup')
// }
const goToSignup = () => {
    console.log('Navigating to signup page...');
    // Here you would typically navigate to the signup page,
    // e.g., using Vue Router.
    alert('Redirecting to signup page...');
};
</script>

<style scoped>
/* You can add component-specific styles here */
</style>
