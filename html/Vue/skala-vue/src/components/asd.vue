<template>
  <div class="m-3">
    <h3 class="bmi-title">홍길동의 BMI 계산기</h3>
    <div class="mb-2">
      <label for="heightInput" class="form-label">키 (cm)</label>
      <input v-model="height" id="heightInput" type="number" class="form-control">
    </div>
    <div class="mb-2">
      <label for="weightInput" class="form-label">체중 (kg)</label>
      <input v-model="weight" id="weightInput" type="number" class="form-control">
    </div>
    <div class="mt-3">
      <p>BMI 지수: <span class="bmi-value">{{ bmi.toFixed(2) }}</span></p>
      <p>판정: <span :style="bmiResult.style">{{ bmiResult.message }}</span></p>
    </div>
  </div>
</template>
<script setup>
// Vue의 반응성 API들을 임포트합니다.
import { ref, computed } from "vue";
// 키(height)를 반응형 데이터로 선언하고 초기값 170cm를 설정합니다.
const height = ref(170);
// 체중(weight)을 반응형 데이터로 선언하고 초기값 60kg를 설정합니다.
const weight = ref(60);
// BMI(체질량지수)를 계산하는 computed 속성을 정의합니다.
// height나 weight 값이 변경될 때마다 자동으로 재계산됩니다.
const bmi = computed(() => {
  // 키나 체중이 0 이하일 경우 BMI 계산을 방지하고 0을 반환합니다.
  if (height.value <= 0 || weight.value <= 0) return 0;
  // BMI 계산 공식: 체중(kg) / (키(m) * 키(m))
  return weight.value / ((height.value / 100) * (height.value / 100));
});

// BMI 값에 따라 메시지와 스타일을 반환하는 computed 속성입니다.
const bmiResult = computed(() => {
  const bmiValue = bmi.value;
  if (bmiValue <= 0) {
    return { message: '키와 체중을 입력해주세요.', style: { color: 'grey' } };
  }
  if (bmiValue < 18.5) {
    return { message: "저체중", style: { color: '#3498db', fontWeight: 'bold' } };
  }
  else if (bmiValue < 23) {
    return { message: "정상", style: { color: '#2ecc71', fontWeight: 'bold' } };
  }
  else if (bmiValue < 25) {
    return { message: "과체중", style: { color: '#f39c12', fontWeight: 'bold' } };
  }
  else {
    return { message: "비만", style: { color: '#e74c3c', fontWeight: 'bold' } };
  }
});
</script>
<style scoped>
.bmi-title {
  background: linear-gradient(to right, #42b983, #347474);
  -webkit-background-clip: text;
  background-clip: text;

  color: transparent;
  font-weight: bold;
}

.bmi-value {
  font-weight: bold;
  color: #34495e;
}

.form-control:focus {
  border-color: #42b983;
  box-shadow: 0 0 0 0.25rem rgba(66, 185, 131, 0.25);
}
</style>
