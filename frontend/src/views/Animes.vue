<template>
  <div v-if="getUser && !getAnimesData.count == 0" class="container animes">
    <div
      class="container mb-3"
      v-for="anime in getAnimesData.results"
      :key="anime.id"
    >
      <div class="card anime-cards p-3">
        <div class="card-title">
          <h4>{{ anime.english_name }}</h4>
        </div>
        <div class="card-body row">
          <div class="col-12 col-lg-2">
            <img class="animes-cover-images" :src="anime.cover_image" />
          </div>
          <div class="col-12 col-lg-10 mt-3">
            <h6 class="animes-descriptions" v-if="anime.description">
              {{ anime.description }}
            </h6>
            <h6 class="animes-descriptions" v-if="!anime.description">
              No description available yet (」°ロ°)
            </h6>
          </div>
        </div>
      </div>
    </div>
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
  <div v-else class="container animes">
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
.animes-descriptions {
  text-align: justify;
  display: -webkit-box;
  overflow: hidden;
  -webkit-line-clamp: 5;
  -webkit-box-orient: vertical;
  -webkit-box-align: center;
}
.animes-cover-images {
  max-width: 65%;
  border-radius: 5px;
}
.anime-cards:hover {
  box-shadow: 0 2px 5px 0 rgba(79, 82, 87, 0.5),
    0 2px 10px 0 rgba(79, 82, 87, 0.5);
}
.animes {
  margin-bottom: 7rem;
  margin-top: 15rem;
}
</style>