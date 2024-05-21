<template>
  <div>
    <RouterLink :to="{ name: 'DepositList' }" >예금 상품</RouterLink>
    <RouterLink :to="{ name: 'SavingList' }" >적금 상품</RouterLink>
    <div class="container border">
      <RouterView />
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>

</style>
