<script setup>
import {ref, reactive, watch, onMounted} from 'vue';
import apiCall from '@/scripts/api-call';

import PageNavigator from '@/components/PageNavigator.vue';
import InlineInput from '@/components/InlineInput.vue';
import ItemsTable from '@/components/ItemsTable.vue';
//import { get } from 'node:https';

const stockName = ref('');
const stockPrice = ref('');
const table = reactive({
 headers: [
 { label: "주식ID", value: "id" },
 { label: "주식명", value: "stockName" },
 { label: "주식가격", value: "stockPrice" },
 ],
 items: []
 })

const page = reactive({
  total: 0,
  current: 1,
  count: 10,
})

const getStockList = async() => {
  const url = `/api/stocks/list`;
  const queryParam = {
    offset: page.current-1,
    count: page.count
  }
  const response = await apiCall.get(url, null, queryParam);
  if (response.result === apiCall.Response.SUCCESS) {
    console.log(response.body)
    
    const pagedList = response.body;
    table.items = pagedList.list;
    page.total = pagedList.total;
  } else {
    notifyInfo(response.message);
  }
}

const addStock = async() => {
  const url = '/api/stocks';
  const requestBody = {
    id:0,
    stockName: stockName.value,
    stockPrice: stockPrice.value
  }

  const response = await apiCall.post(url, null, requestBody);

  if (response.result === apiCall.Response.SUCCESS) {
    
    table.items.push(response.body);
    getStockList();
    stockName.value = '';
    stockPrice.value = '';
    notifySuccess('주식이 추가되었습니다.');
  } else {
    notifyInfo(response.message);
  }
}

watch(() => page.current, getStockList);
watch(() => page.count, () => {page.current = 1; getStockList()});

onMounted(getStockList);


</script>

<template>
  <div class="row mt-2">
    <span class="fs-4"><i class="bi bi-graph-up m-2"></i>주식목록</span>
  </div>
  <div class="row border-bottom">
    <div class="col d-flex justify-content-end">
      <button @click="getStockList" class="btn btn-sm btn-primary m-1">
        <i class="bi bi-arrow-counterclockwise m-2"></i>갱신</button>
    </div>
  </div>
  <div class="row g-2 align-items-center m-2 mt-0">
    <div class="col">
      <ItemsTable :nosetting="true" :headers="table.headers" :items="table.items" />
      <PageNavigator v-model:current="page.current" v-model:count="page.count" :totalCount="page.total" />
    </div>
  </div>
  <div class="row g-2 m-2 border-top">
    <div class="col-2 d-flex justify-content-end">
      <label class="col-form-label form-control-sm p-1">주식정보</label>
    </div>
    <div class="col">
      <InlineInput v-model="stockName" placeholder="주식명"/>
    </div>
    <div class="col">
      <InlineInput v-model="stockPrice" placeholder="주식가격"/>
    </div>
    <div class="col d-flex justify-content-start">
      <button @click="addStock" class="btn btn-sm btn-outline-primary me-2">주식 추가</button>
    </div>
  </div>
</template>
