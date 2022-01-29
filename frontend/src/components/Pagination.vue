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
import { mapGetters } from "vuex";

export default {
  name: "Pagination",
  methods: {
    async getNextPage() {
      const response = await getData(this.getAnimesData.next);
      this.$store.dispatch("updateAnimesData", response.data);
      scrollTo(0, 0);
    },
    async getPreviousPage() {
      const response = await getData(this.getAnimesData.previous);
      this.$store.dispatch("updateAnimesData", response.data);
      scrollTo(0, 0);
    },
  },
  computed: {
    ...mapGetters(["getAnimesData"]),
  },
};
</script>