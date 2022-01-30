<template>
  <div class="container">
    <button
      v-if="getAnimesData.previous"
      class="btn btn-primary me-2"
      @click="getPreviousPage"
    >
      Previous
    </button>
    <button
      v-if="getAnimesData.next"
      class="btn btn-primary"
      @click="getNextPage"
    >
      Next
    </button>
  </div>
</template>

<script>
import { getData } from "../api";
import { mapGetters, mapState } from "vuex";

export default {
  name: "Pagination",
  data() {
    return {
      page: 1,
    };
  },
  methods: {
    async getNextPage() {
      this.page++;
      const response = await getData(this.getAnimesData.next);
      this.$store.dispatch("updateAnimesData", response.data);
      scrollTo(0, 0);
      if (isNaN(this.getUserInput)) {
        this.$router.push({
          name: "Pagination",
          params: { data: this.getUserInput, page: this.page },
        });
      } else {
        this.$router.push({
          name: "Pagination",
          params: { page: this.page },
        });
      }
    },
    async getPreviousPage() {
      this.page--;
      const response = await getData(this.getAnimesData.previous);
      this.$store.dispatch("updateAnimesData", response.data);
      scrollTo(0, 0);
      if (isNaN(this.getUserInput)) {
        this.$router.push({
          name: "Pagination",
          params: { data: this.getUserInput, page: this.page },
        });
      } else {
        this.$router.push({
          name: "Pagination",
          params: { page: this.page },
        });
      }
    },
  },
  computed: {
    ...mapGetters(["getAnimesData"]),
    ...mapGetters(["getUserInput"]),
    ...mapState(["userInput"]),
  },
  watch: {
    userInput(newValue, oldValue) {
      if (oldValue != newValue) {
        this.page = 1;
      }
    },
  },
};
</script>