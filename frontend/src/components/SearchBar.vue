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
import axios from "axios";
import { mapGetters } from "vuex";

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
      this.$router.push({
        name: "AnimeList",
        query: { name: this.getUserInput, score: "any", page: 1 },
      });
      if (this.$route.name != "AnimeList") {
        const response = await axios.get(
          `api-v1/animes/?search=${this.getUserInput}`
        );
        this.$store.dispatch("updateAnimesData", response.data);
      }
      this.userInput = "";
    },
  },

  computed: {
    ...mapGetters(["getUserInput"]),
  },
};
</script>