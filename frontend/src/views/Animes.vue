<template>
  <div
    v-if="getUser && !getAnimesData.count == 0"
    class="container animes-wrapper"
  >
    <div class="row mb-5">
      <div
        class="container mb-3 col-6 col-lg-2"
        v-for="anime in getAnimesData.results"
        :key="anime.id"
      >
        <div class="anime-card card border-0">
          <div class="anime-cover-image"></div>
          <img class="anime-cover-image" :src="anime.cover_image" />
          <p class="anime-name">
            <strong>{{ anime.english_name }}</strong>
          </p>
        </div>
      </div>
    </div>
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
  </div>
  <div v-else class="container animes-wrapper">
    <Error :message="errorMessage" />
  </div>
</template>

<script>
import Error from "../components/Error.vue";
import { mapGetters } from "vuex";
import { getData } from "../api";

export default {
  name: "Animes",
  components: {
    Error,
  },
  data() {
    return {
      errorMessage: "No results found for your search",
    };
  },
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
    ...mapGetters(["getUser"]),
    ...mapGetters(["getAnimesData"]),
    ...mapGetters(["getUserInput"]),
  },
  async created() {
    try {
      const response = await getData(
        `api-v1/animes/?search=${this.getUserInput}`
      );
      this.$store.dispatch("updateAnimesData", response.data);
    } catch (e) {
      this.errorMessage = "You first need to login to access to all the animes";
    }
  },
};
</script>

<style>
.animes-wrapper {
  margin-bottom: 7rem;
  margin-top: 15rem;
}
.anime-card {
  transition: 0.4s ease-out;
}
.anime-card:hover {
  transition: 0.4s ease-out;
  opacity: 0.8;
}
.anime-name {
  text-align: left;
}
.anime-cover-image {
  border-radius: 5px;
  max-width: 196px;
  max-height: 270px;
  width: auto;
  height: auto;
}
</style>