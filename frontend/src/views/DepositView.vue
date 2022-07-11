<template>
  <div class="about">
    <div class="max-w-sm rounded overflow-hidden shadow-lg">
      <div class="px-6 py-4">
        <div class="font-bold text-xl mb-2">Deposit</div>

        <div class="md:flex md:items-center mb-6">
          <div class="md:w-1/3">
            <label
              class="
                block
                text-gray-500
                font-bold
                md:text-right
                mb-1
                md:mb-0
                pr-4
              "
              for="inline-full-name"
            >
              Amount
            </label>
          </div>
          <div class="md:w-2/3">
            <input
              class="
                bg-gray-200
                appearance-none
                border-2 border-gray-200
                rounded
                w-full
                py-2
                px-4
                text-gray-700
                leading-tight
                focus:outline-none focus:bg-white focus:border-purple-500
              "
              id="inline-full-name"
              type="text"
              v-model="amount"
            />
          </div>
        </div>
        <div class="md:flex md:items-center">
          <div class="md:w-1/3"></div>
          <div class="md:w-2/3">
            <button
              id="create"
              class="
                bg-purple-500
                hover:bg-purple-700
                text-white
                font-bold
                py-2
                px-4
                rounded
              "
              @click="deposit"
            >
              Deposit
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import fs from "fs";
import Web3 from "web3";
import abi from "../assets/Bank.json";
const web3 = new Web3((window as any).web3.currentProvider);

//local contract
var contract = new web3.eth.Contract(
  abi.abi,
  "0x43cbD0E8b1b143B8E489711d99c1834aCC1cA061"
);
export default {
  props: {
    address: "",
  },
  data() {
    return {
      amount: "",
    };
  },
  methods: {
    async deposit() {
      console.log(this.address);
      await contract.methods
        .deposit(this.amount)
        .send({ from: this.address })
        .then((result) => {
          console.log(result);
        });
      await contract.methods
        .getAccountList()
        .call()
        .then((result) => {
          console.log(result);
        });
    },
  },
};
</script>


<style>
</style>