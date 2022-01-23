<template>
  <form @submit.prevent="getUserSearch" class="col-12 col-lg-auto mb-3 mb-lg-0">
    <input
      v-model="user_input"
      type="search"
      class="form-control"
      placeholder="Search..."
      aria-label="Search"
    />
  </form>
</template>

<script>
import { mapGetters } from "vuex";
import { getData } from "../api";

export default {
  name: "SearchBar",
  data() {
    return {
      user_input: "",
    };
  },
  methods: {
    async getUserSearch() {
      this.$store.dispatch("updateUserInput", this.user_input);
      if (this.$route.name == "Animes") {
        const response = await getData(
          `api-v1/animes/?search=${this.getUserInput}`
        );
        this.$store.dispatch("updateAnimesData", response.data);
      } else {
        this.$router.push("Animes");
      }
      this.user_input = "";
    },
  },
  computed: {
    ...mapGetters(["getUserInput"]),
  },
};
</script>