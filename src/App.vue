<script setup>
import {ref} from 'vue'
const isLogIn = ref(false);
if (localStorage.getItem("username")&&localStorage.getItem("password")){
  isLogIn.value = true;
}
</script>

<template>
  <header>
    <div>TwitterClone</div>
    <div v-if="isLogIn">
      <img src="">
      <div>
        <button @click="logOut()">Выйти</button>
      </div>
    </div>
    <div v-else>
        <button @click="logIn()">Log in</button>
    </div>
  </header>

  <main>
=  </main>
</template>

<style scoped>

</style>
