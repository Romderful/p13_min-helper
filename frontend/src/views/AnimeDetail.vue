<template>
  <div
    v-if="animeData.description"
    v-html="animeData.description"
    class="container"
  ></div>
  <div v-else class="container">
    <p>We're sorry, the description isn't available yet.</p>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import { getData } from "../api";

export default {
  name: "AnimeDetail",
  props: ["id"],
  data() {
    return {
      animeData: [],
    };
  },
  computed: {
    ...mapGetters(["getAnimesData"]),
  },
  async created() {
    const response = await getData(`api-v1/animes/${this.id}/`);
    this.animeData = response.data;
  },
};
</script>