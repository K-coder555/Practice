// import { createRouter, createWebHistory } from "vue-router";
// import DisguiseMenu from "./pages/DisguiseMenu.vue";
// import DisguisePage from "./pages/DisguisePage.vue";

// import DisguiseMenu from "./pages/DisguiseMenu.vue";

// const routes = [
//  {
//  path: "/",
//  name: "DisguiseMenu",
//  component: DisguiseMenu,
//  },
//  {
//  path: "/disguise",
//  name: "Disguise",
//  component: DisguisePage,
//  },
//  ];
// const router = createRouter({
//  history: createWebHistory(),
//  routes,
//  });
// export default router;


import { createRouter, createWebHistory } from "vue-router";
 import LoginPage from "./pages/LoginPage.vue";
 import SignupPage from "./pages/SignupPage.vue";
 import MainPage from "./pages/MainPage.vue";
 import MainPage2 from "./pages/MainPage2.vue";
 import DisguisePage from "./pages/DisguisePage.vue";

 import DisguiseMenu from "./pages/DisguiseMenu.vue";

 const routes = [
    { path: "/", component: MainPage2, children: [
        // Add a child route for the disguise page to be displayed within MainPage2
        { path: "disguise/:target", name: "disguise", component: DisguisePage, props: true },
        // Optional: a default view when no target is selected
        { path: "disguise", component: DisguisePage }
    ] },
    { path: "/login", component: LoginPage },
    { path: "/signup", component: SignupPage },
    { path: "/main-feed", component: MainPage }, // Old main page, new path
    { path: "/:pathMatch(.*)*", redirect: "/" },
    { path: "/disguise-menu", component: DisguiseMenu },
    //{ path: "/login", component: LoginPage },
 ];

 const router = createRouter({
    history: createWebHistory(),
    routes,
 });

 export default router;