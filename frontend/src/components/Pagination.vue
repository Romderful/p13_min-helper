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
import { mapGetters } from "vuex";

export default {
  name: "Pagination",
  data() {
    return {
      page: 1,
    };
  },
  methods: {
    async getNextPage() {
      this.page = this.$route.query.page;
      this.page++;
      const query = { ...this.$route.query, page: this.page };
      this.$router.push({ query });
    },
    async getPreviousPage() {
      this.page = this.$route.query.page;
      this.page--;
      const query = { ...this.$route.query, page: this.page };
      this.$router.push({ query });
    },
  },
  computed: {
    ...mapGetters(["getAnimesData"]),
    ...mapGetters(["getUserInput"]),
  },
};
</script>