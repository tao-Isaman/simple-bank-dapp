<script setup lang="ts">
import { useMetaMaskWallet } from 'vue-connect-wallet'
import { RouterLink, RouterView } from 'vue-router'
import { computed, defineComponent, onMounted, ref } from 'vue';

const isLogin = ref(false)
const address = ref("")
const isMetamaskSupport = ref(false)

onMounted(() => {
  isMetamaskSupport.value = typeof(window as any).ethereum !== "undefined"
})

async function connectWallet() {
  const account = await (window as any).ethereum.request({method : "eth_requestAccounts"});
  address.value = account[0]
  console.log(address)
}

const computeAddress = computed(() => "connected to " + address.value.substring(0,6) + "...")



</script>

<template>
<div>
  <div class="flex justify-end pt-5 pr-5">
        <button id="address" class="bg-purple-500 hover:bg-purple-700 text-white font-bold py-2 px-4 rounded" @click="connectWallet">
        {{address === "" ? "connect wallet" : computeAddress}}
      </button>
    </div>

<div class="flex justify-center">
    <img alt="Vue logo" class="logo" src="./assets/logo.png" width="250" height="125" />
      <div >
      <h1 class="violet text-2xl pt-14">SCB10X BlockChain Camp 2022</h1>
      <nav class="violet">
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/create">Create Account</RouterLink>
        <RouterLink to="/deposit">Deposit</RouterLink>
        <RouterLink to="/tranfer">Tranfer</RouterLink>
        <RouterLink to="/multi-tranfer">Multiple Tranfer</RouterLink>
      </nav>
    </div>
</div>
<div class="flex justify-center">
  <RouterView />
</div>
</div>
</template>

<style>
@import './assets/base.css';

.logo {
  display: block;
  margin: 0 auto 2rem;
}

.violet {
  text-decoration: none;
  color: rgb(120, 0, 189);
  transition: 0.4s;
}

@media (hover: hover) {
  a:hover {
    background-color: hsla(160, 100%, 37%, 0.2);
  }
}

nav {
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {

  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
