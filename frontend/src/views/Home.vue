<template>
  <div class="container">
    <h1>Home</h1>
    <hr />
    <h3 v-if="user">Welcome {{ user.username }}</h3>
    <h3 v-if="!user">Welcome guest</h3>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Home",
  computed: {
    ...mapGetters(["user"]),
  },
};
</script>