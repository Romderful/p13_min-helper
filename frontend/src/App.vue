<template>
  <Navbar />
  <router-view />
</template>

<script>
import Navbar from "./components/Navbar.vue";
import axios from "axios";

export default {
  name: "App",
  components: {
    Navbar,
  },
  async created() {
    const response = await axios.get("api-v1/auth/user/", {
      headers: {
        Authorization: "Bearer " + localStorage.getItem("access_token"),
      },
    });
    this.$store.dispatch("user", response.data);
  },
};
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>