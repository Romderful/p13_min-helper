<template>
  <div v-if="data.links" class="container">
    <button
      v-if="data.links.previous"
      class="btn btn-primary me-2"
      @click="getPreviousPage"
    >
      Previous
    </button>
    <button v-if="data.links.next" class="btn btn-primary" @click="getNextPage">
      Next
    </button>
    <div v-if="!data.count == 0" class="container mt-3">
      <i>page {{ data.current_page_number }} out of {{ data.total_pages }}</i>
    </div>
  </div>
</template>

<script>
export default {
  name: "Pagination",
  props: ["data"],

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
};
</script>