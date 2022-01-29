<template>
  <footer class="footer">
    <div class="container">
      <router-link :to="{ name: 'About' }" class="nav-link link-dark px-2"
        >About</router-link
      >
    </div>
  </footer>
</template>

<style>
.footer {
  position: fixed;
  bottom: 0;
  width: 100%;
  height: 60px;
  line-height: 60px;
  background-color: #f5f5f5;
}
</style>
