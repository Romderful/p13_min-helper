<template>
  <div class="alert alert-danger">
    <p>{{ message }}</p>
  </div>
</template>

<script>
export default {
  name: "Error",
  props: ["message"],
};
</script>