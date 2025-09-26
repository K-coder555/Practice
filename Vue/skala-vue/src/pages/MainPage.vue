<template>
    <div class="container mt-4">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div v-if="posts.length === 0" class="text-center">
                    <p>No posts to display.</p>
                </div>
                <div v-else>
                    <div v-for="post in posts" :key="post.id" class="card mb-4">
                        <img :src="post.imageUrl" class="card-img-top" :alt="`Post by user ${post.id}`">
                        <div class="card-body">
                            <div class="d-flex justify-content-start align-items-center mb-2">
                                <button class="btn btn-outline-danger btn-sm" @click="toggleLike(post)">
                                    <i class="bi" :class="post.liked ? 'bi-heart-fill' : 'bi-heart'"></i> Like
                                </button>
                                <span class="ms-2">{{ post.likes }} likes</span>
                            </div>
                            <div class="comments-section">
                                <div v-for="(comment, index) in post.comments" :key="index" class="mb-1">
                                    <strong>User{{ index + 1 }}:</strong> {{ comment }}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';

// Mock data for posts
const posts = ref([
    {
        id: 1,
        imageUrl: 'https://picsum.photos/seed/picsum1/600/400',
        comments: ['This is a great photo!', 'Amazing view.'],
        likes: 12,
        liked: false
    },
    {
        id: 2,
        imageUrl: 'https://picsum.photos/seed/picsum2/600/400',
        comments: ['Love this place.'],
        likes: 5,
        liked: true
    },
    {
        id: 3,
        imageUrl: 'https://picsum.photos/seed/picsum3/600/400',
        comments: ['So beautiful!', 'I want to go there.', 'Nice shot!'],
        likes: 23,
        liked: false
    }
]);

const toggleLike = (post) => {
    post.liked = !post.liked;
    if (post.liked) {
        post.likes++;
    } else {
        post.likes--;
    }
};

</script>

<style scoped>
.card-img-top {
    max-height: 500px;
    object-fit: cover;
}
.comments-section {
    font-size: 0.9rem;
}
/* Make sure you have Bootstrap Icons included in your project for the heart icon */
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css");
</style>