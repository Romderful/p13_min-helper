<template>
  <div class="container mb-5" v-if="getUser">
    <div class="container row" style="max-width: 600px; margin: auto">
      <div class="container col-lg-6 col-12 mb-3">
        <label class="form-label"><b>Genres</b></label>
        <input
          class="form-control"
          list="datalistOptions"
          placeholder="any"
          v-model="selectedGenre"
          @change="goToGenre(selectedGenre)"
        />
        <datalist id="datalistOptions">
          <option v-for="category in categoriesData" :key="category.id">
            {{ category.name }}
          </option>
        </datalist>
      </div>
      <div class="container col-lg-6 col-12">
        <label class="form-label"><b>Scoring</b></label>
        <select
          v-model="selectedScore"
          @change="goToScore(selectedScore)"
          class="form-select"
          aria-label="Default select example"
        >
          <option value="any">any</option>
          <option value="-score">best</option>
          <option value="score">lowest</option>
        </select>
      </div>
    </div>
  </div>
  <div v-if="getUser" class="container animes-wrapper">
    <div class="row mb-3">
      <transition-group name="fade" appear>
        <div
          class="container mb-3 col-6 col-lg-2"
          v-for="anime in getAnimesData"
          :key="anime.id"
        >
          <router-link
            class="router-link"
            :to="{ name: 'AnimeDetail', params: { id: anime.id } }"
          >
            <div class="anime-card card border-0">
              <img class="anime-cover-image" :src="anime.cover_image" />
              <p class="anime-name">
                <strong>{{ anime.english_name }}</strong>
              </p>
            </div></router-link
          >
        </div>
      </transition-group>
    </div>
    <!-- <Pagination /> -->
  </div>
  <div v-else class="container">
    <Error :message="errorMessage" />
  </div>
</template>

<script>
import Error from "../components/Error.vue";
// import Pagination from "../components/Pagination.vue";
import { mapGetters } from "vuex";
import { getData } from "../api";

export default {
  name: "AnimeList",
  components: {
    Error,
    // Pagination,
  },
  watch: {
    async $route() {
      if (this.$route.query.genre) {
        if (this.$route.query.score) {
          const response = await getData(
            `api-v1/animes/?categories=${this.$route.query.genre}&ordering=${this.$route.query.score}`
          );
          this.$store.dispatch("updateAnimesData", response.data.results);
        } else {
          const response = await getData(
            `api-v1/animes/?categories=${this.$route.query.genre}`
          );
          this.$store.dispatch("updateAnimesData", response.data.results);
        }
      } else if (!this.$route.query.genre) {
        if (this.$route.query.score) {
          const response = await getData(
            `api-v1/animes/?ordering=${this.$route.query.score}`
          );
          this.$store.dispatch("updateAnimesData", response.data.results);
        } else {
          if (this.$route.query.name) {
            const response = await getData(
              `api-v1/animes/?search=${this.$route.query.name}`
            );
            this.$store.dispatch("updateAnimesData", response.data.results);
            this.selectedScore = "any";
            this.selectedGenre = null;
          } else {
            const response = await getData("api-v1/animes/");
            this.$store.dispatch("updateAnimesData", response.data.results);
            this.selectedScore = "any";
            this.selectedGenre = null;
          }
        }
      }
    },
  },
  data() {
    return {
      errorMessage: "No data could be found",
      categoriesData: null,
      selectedGenre: null,
      selectedScore: "any",
    };
  },
  methods: {
    async getCategories() {
      const response = await getData("api-v1/animes-categories/");
      this.categoriesData = response.data.results;
    },
    goToGenre(genre) {
      if (this.selectedScore) {
        this.$router.push({
          query: { genre: genre, score: this.selectedScore },
        });
      } else {
        this.$router.push({ query: { genre: genre } });
      }
    },
    goToScore(score) {
      if (this.selectedGenre) {
        this.$router.push({
          query: { genre: this.selectedGenre, score: score },
        });
      } else {
        this.$router.push({
          query: { score: score },
        });
      }
    },
  },
  computed: {
    ...mapGetters(["getUser"]),
    ...mapGetters(["getAnimesData"]),
    ...mapGetters(["getUserInput"]),
  },
  async created() {
    this.getCategories();
  },
};
</script>

<style>
.animes-wrapper {
  margin-bottom: 7rem;
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
}
.fade-enter-active,
.fade-leave-active {
  transition: all 1s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
.router-link {
  text-decoration: none;
  color: black;
}
</style>