<template>
  <form @submit.prevent="getUserSearch" class="col-12 col-lg-auto mb-3 mb-lg-0">
    <input
      v-model="userInput"
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
      userInput: "",
    };
  },
  methods: {
    async getUserSearch() {
      this.$store.dispatch("updateUserInput", this.userInput);
      this.$router.push({ name: "AnimeList" });
      const response = await getData(
        `api-v1/animes/?search=${this.getUserInput}`
      );
      this.$store.dispatch("updateAnimesData", response.data);
      this.userInput = "";
    },
  },
  computed: {
    ...mapGetters(["getUserInput"]),
  },
};
</script>