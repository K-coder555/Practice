<script setup>
 import { ref, isRef, reactive, isReactive, toRaw, unref } from 'vue'


 function toJsonString(data) {
  // 1. Unwrap ref objects to get their inner value.
  const unwrappedData = isRef(data) ? unref(data) : data;

  // 2. Convert reactive proxies to raw, plain JavaScript objects.
  const rawData = isReactive(unwrappedData) ? toRaw(unwrappedData) : unwrappedData;

  // 3. Use JSON.stringify for standard serialization.
  // The third argument (2) is for pretty-printing the JSON.
  
  return JSON.stringify(rawData, null, 2);
}
 const num = 123
 const obj = { name: '홍길동', age: 30 }
 const arr = [1, 2, 3]
 const r1 = ref({ city: '서울' })
 const r2 = reactive({ job: '개발자' })
 console.log(toJsonString(num), toJsonString(obj), toJsonString(arr), toJsonString(r1), toJsonString(r2))
 const result = reactive([])
 result.push(toJsonString(num))
 result.push(toJsonString(obj))
 result.push(toJsonString(arr))
 result.push(toJsonString(r1))
 result.push(toJsonString(r2))
 </script>
<template>
    <div>
        {{ result.join() }}
    </div>
</template>