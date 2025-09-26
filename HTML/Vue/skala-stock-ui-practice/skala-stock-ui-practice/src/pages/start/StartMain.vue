<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import apiCall from '@/scripts/api-call';
import { storePlayer } from '@/scripts/store-player';
import { notifyInfo, notifySuccess } from '@/scripts/store-popups';
import InlineInput from '@/components/InlineInput.vue';
//import { url } from 'inspector';

const router = useRouter();
const isNewPlayer = ref(false);
const playerId = ref('');
const playerPassword = ref('');
//const url = ref('');

const login = async () => {
  const url = '/api/players/login';
  const requestBody = {
    playerId: playerId.value,
    playerPassword: playerPassword.value,
  }
  if (!playerId.value || !playerPassword.value) {
    notifyInfo('플레이어ID와 비밀번호를 입력해주세요.');
    return;
  }

  const response = await apiCall.post(url, null, requestBody)
  
  if (response.result === apiCall.Response.SUCCESS) {
    console.log('Login Response:', response.body);
    storePlayer(response.body);
    router.push('/stock');
  } else {
    notifyInfo('로그인에 실패했습니다. ' + response.message);
    isNewPlayer.value = true;
    playerId.value = '';
    playerPassword.value = '';
  }
};

const register = async () => {
  const url = '/api/players'
  const requestBody = {
    playerId: playerId.value,
    playerPassword: playerPassword.value,
    playerMoney: 0
  }
  if (!playerId.value || !playerPassword.value) {
    notifyInfo('플레이어ID와 비밀번호를 입력해주세요.');
    return;
  }

  const response = await apiCall.post(url, null, requestBody);

  if (response.result === apiCall.Response.SUCCESS) {
    notifySuccess('회원가입이 완료되었습니다. 로그인을 진행해주세요.');
    isNewPlayer.value = false;
    playerId.value = '';
    password.value = '';
  } else {
    notifyInfo('회원가입에 실패했습니다. ' + response.message);
    playerId.value = '';
    password.value = '';

  }
};
</script>

<template>
  <div class="container-sm mt-3 border border-2 p-1" style="max-width: 600px">
    <div class="bss-background p-1">
      <div class="mt-3 d-flex justify-content-center" style="height: 230px;">
        <span class="text-center text-danger fs-1 fw-bold mt-4">SKALA STOCK Market</span>
      </div>
      <div class="row bg-info-subtle p-2 m-1" style="opacity: 95%;">
        <div class="col">
          <InlineInput label="플레이어ID" class="mb-1" type="text" placeholder="플레이어ID" v-model="playerId" />
          <InlineInput label="비밀번호" class="mb-1" type="password" placeholder="비밀번호" v-model="playerPassword" />
        </div>
        <div class="d-flex justify-content-end">
          <button class="btn btn-primary btn-sm" @click="register">회원가입</button>
          <button class="btn btn-primary btn-sm" @click="login">로그인</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.bss-background {
  width: 590px;
  height: 380px;
  background-image: url('/logo.png');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}
</style>