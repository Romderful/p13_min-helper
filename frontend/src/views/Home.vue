<template>
  <div class="container">
    <h1>Home</h1>
    <hr />
    <h3>Welcome {{ username }}</h3>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Home",
  data() {
    return {
      username: "",
    };
  },
  async created() {
    const response = await axios.get("api-v1/auth/user/", {
      headers: {
        Authorization: "Bearer " + localStorage.getItem("access_token"),
      },
    });
    this.username = response.data.username;
  },
};
</script>