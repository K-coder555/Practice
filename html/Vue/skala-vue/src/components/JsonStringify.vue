<template>
  <div>
    <h2>JSON Stringify Test</h2>
    <pre>{{ jsonOutput }}</pre>
  </div>
</template>

<script setup>
import { ref, reactive, computed } from 'vue';
import { isRef, isReactive, toRaw } from 'vue';

/**
 * Safely converts any JavaScript value (including Vue's ref and reactive)
 * to a JSON string.
 *
 * @param {*} data The input data to convert.
 * @returns {string} A JSON string representation of the data.
 */
function toJsonString(data) {
  // 1. Unwrap ref objects to get their inner value.
  const unwrappedData = isRef(data) ? data.value : data;

  // 2. Convert reactive proxies to raw, plain JavaScript objects.
  const rawData = isReactive(unwrappedData) ? toRaw(unwrappedData) : unwrappedData;

  // 3. Use JSON.stringify for standard serialization.
  // The third argument (2) is for pretty-printing the JSON.
  return JSON.stringify(rawData, null, 2);
}

// --- Example Usage ---

// 1. Primitive types
const myString = 'Hello Vue';
const myNumber = 123;
const myBoolean = ref(true); // ref primitive

// 2. Array
const myArray = reactive(['apple', 'banana', 'cherry']);

// 3. Plain JavaScript Object
const myObject = { id: 1, name: 'Plain Object' };

// 4. Reactive Object
const myReactiveObject = reactive({
  id: 2,
  name: 'Reactive Object',
  nested: {
    items: [1, 2, 3]
  }
});

// 5. Ref holding an object
const myRefObject = ref({
  id: 3,
  name: 'Ref Object'
});

// Combine all examples into one object for display
const testData = {
  string: myString,
  number: myNumber,
  boolean: myBoolean,
  array: myArray,
  plainObject: myObject,
  reactiveObject: myReactiveObject,
  refObject: myRefObject,
  nullValue: null,
  undefinedValue: undefined, // Note: undefined properties are omitted in JSON
};

// Use a computed property to display the JSON output
const jsonOutput = computed(() => toJsonString(testData));

</script>

<style scoped>
pre {
  background-color: #f4f4f4;
  border: 1px solid #ddd;
  padding: 1rem;
  border-radius: 4px;
  white-space: pre-wrap;
  word-wrap: break-word;
}
</style>
