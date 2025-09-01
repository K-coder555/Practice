<template>

<div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card">
                    <div class="card-header">
                        <h3 class="text-center">Sign Up</h3>
                    </div>
                    <div class="card-body">
                        <form @submit.prevent="handleSignup">
                            <div class="mb-3">
                                <label for="name" class="form-label">Name</label>
                                <input type="text" class="form-control" id="name" v-model="form.name" required>
                            </div>

                            <div class="mb-3">
                                <label class="form-label">Gender</label>
                                <CommonRadio 
                                    name="gender"
                                    option-set="gender"
                                    v-model="form.gender"
                                />
                            </div>

                            <div class="mb-3">
                                <label for="email" class="form-label">Email address</label>
                                <input type="email" class="form-control" id="email" v-model="form.email" required>
                            </div>

                            <div class="mb-3">
                                <label for="password" class="form-label">Password</label>
                                <input type="password" class="form-control" id="password" v-model="form.password" required>
                            </div>

                            <div class="mb-3">
                                <label for="passwordConfirm" class="form-label">Confirm Password</label>
                                <input type="password" class="form-control" id="passwordConfirm" v-model="form.passwordConfirm" required>
                            </div>

                            <div class="d-grid gap-2">
                                <button type="submit" class="btn btn-primary">Sign Up</button>
                                <button type="button" class="btn btn-secondary" @click="goToLogin">Go to Login</button>
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
import {useRouter} from 'vue-router';
import CommonRadio from '../commons/CommonRadio.vue';

const form = ref({
    name: '',
    gender: 'm', // Default to male
    email: '',
    password: '',
    passwordConfirm: ''
});
const router = useRouter()
// function useRouter() {
//     router.push('/login')
// }
const handleSignup = () => {
    if (form.value.password !== form.value.passwordConfirm) {
        alert("Passwords do not match!");
        return;
    }

    console.log('Signing up with:', form.value);
    // Here you would typically handle the signup logic,
    // e.g., by calling an API.
    alert(`Signup successful for ${form.value.name}`);
};

const goToLogin = () => {
    console.log('Navigating to login page...');
    // Here you would typically navigate to the login page,
    // e.g., using Vue Router.
    alert('Redirecting to login page...');
};
</script>

<style scoped>
/* You can add component-specific styles here */
</style>
