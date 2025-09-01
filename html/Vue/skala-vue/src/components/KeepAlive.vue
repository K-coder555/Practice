 <template>
 <div>
 <button @click="selectTab(TabOne)">Tab 1</button>
 <button @click="selectTab(TabTwo)">Tab 2</button>
 <KeepAlive :include="['TabOne', 'TabTwo']">
 <component :is="currentTab" />
 </KeepAlive>
 </div>
 </template>
 <script setup>
 import { ref, markRaw } from 'vue'
 import TabOne from './TabOne.vue'
 import TabTwo from './TabTwo.vue'
 const currentTab = ref(markRaw(TabOne))
 const selectTab = (tab) => {
 currentTab.value = markRaw(tab)
 }
 </script>