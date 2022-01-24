<template>
  <transition name="fade" appear>
    <div class="alert alert-danger">
      <p>{{ message }}</p>
    </div>
  </transition>
</template>

<script>
export default {
  name: "Error",
  props: ["message"],
};
</script>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 2s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>