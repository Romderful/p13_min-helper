<template>
  <div class="container mb-5">
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
          <option v-for="category in categoriesData.results" :key="category.id">
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
        >
          <option value="any">any</option>
          <option value="-score">best</option>
          <option value="score">lowest</option>
        </select>
      </div>
    </div>
  </div>
  <div class="container animes-wrapper">
    <div class="row mb-3">
      <transition-group name="fade" appear>
        <div
          class="container mb-3 col-6 col-lg-2"
          v-for="anime in getAnimesData.results"
          :key="anime.id"
        >
          <div class="anime-card card border-0">
            <div class="image-wrapper card">
              <router-link
                class="router-link"
                :to="{ name: 'AnimeDetail', params: { id: anime.id } }"
                ><img class="anime-cover-image" :src="anime.cover_image"
              /></router-link>
              <svg
                @click="addToFavourites(anime.id)"
                xmlns="http://www.w3.org/2000/svg"
                width="18"
                height="18"
                :fill="anime.is_favourite ? 'red' : 'currentColor'"
                class="bi bi-heart-fill"
                viewBox="0 0 16 16"
              >
                <path
                  fill-rule="evenodd"
                  d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"
                />
              </svg>
            </div>
            <router-link
              class="router-link"
              :to="{ name: 'AnimeDetail', params: { id: anime.id } }"
            >
              <p class="anime-name">
                <strong>{{ anime.english_name }}</strong>
              </p>
            </router-link>
          </div>
        </div>
      </transition-group>
    </div>
    <Pagination />
  </div>
</template>

<script>
import axios from "axios";
import Pagination from "../components/Pagination.vue";
import { mapGetters } from "vuex";

export default {
  name: "AnimeList",
  components: {
    Pagination,
  },

  watch: {
    async $route() {
      if (this.$route.name !== "AnimeList") {
        return;
      }
      this.setAnimesData();
    },
  },

  data() {
    return {
      errorMessage: "No data could be found",
      categoriesData: [],
      selectedGenre: "",
      selectedScore: "any",
      page: 1,
    };
  },

  methods: {
    async getCategories() {
      const response = await axios.get("api-v1/animes-categories/");
      this.categoriesData = response.data;
    },

    goToGenre(genre) {
      this.$route.query.page = 1;
      this.selectedScore = "any";
      if (this.selectedScore) {
        this.$router.push({
          query: {
            genre: genre,
            score: this.selectedScore,
            page: this.$route.query.page,
          },
        });
      } else {
        this.$router.push({
          query: { genre: genre, page: this.$route.query.page },
        });
      }
    },

    goToScore(score) {
      this.$route.query.page = 1;
      if (this.selectedGenre) {
        this.$router.push({
          query: {
            genre: this.selectedGenre,
            score: score,
            page: this.$route.query.page,
          },
        });
      } else {
        if (isNaN(this.getUserInput)) {
          this.$router.push({
            query: {
              name: this.getUserInput,
              score: score,
              page: this.$route.query.page,
            },
          });
        } else {
          this.$router.push({
            query: { score: score, page: this.$route.query.page },
          });
        }
      }
    },

    async setAnimesData() {
      let params = "?";
      if (this.$route.query.genre) {
        params += `categories=${this.$route.query.genre}`;
        this.selectedGenre = this.$route.query.genre;
      } else {
        this.selectedGenre = "";
      }
      if (this.$route.query.score) {
        params += `&ordering=${this.$route.query.score}`;
        this.selectedScore = this.$route.query.score;
      }
      if (this.$route.query.name) {
        params += `&search=${this.$route.query.name}`;
        this.selectedGenre = "";
      }
      params += `&page=${this.$route.query.page}`;
      const response = await axios.get(`api-v1/animes/${params}`);
      this.$store.dispatch("updateAnimesData", response.data);
      window.scrollTo({ top: 0, behavior: "smooth" });
    },

    async addToFavourites(anime_id) {
      const response = await axios.get(`api-v1/animes/${anime_id}/`);
      if (response.data.is_favourite === false) {
        await axios.post("api-v1/animes-favourites/", {
          user: this.getUser.username,
          anime: anime_id,
        });
        response.data.is_favourite = true;
      }
      this.$store.dispatch("updateAnimeData", response.data);
    },
  },

  computed: {
    ...mapGetters(["getUser"]),
    ...mapGetters(["getAnimesData"]),
    ...mapGetters(["getUserInput"]),
  },

  async created() {
    this.getCategories();
    this.setAnimesData();
  },
};
</script>

<style>
.image-wrapper {
  position: relative;
}
.bi-heart-fill {
  position: absolute;
  right: 0;
  margin-top: -0.6rem;
  margin-right: -0.6rem;
}
.bi-heart-fill:hover {
  transition: all 0.4s ease;
  transform: scale(1.5);
  color: red;
}
.animes-wrapper {
  margin-bottom: 7rem;
}
.anime-card {
  transition: 0.4s ease-out;
}
.anime-name {
  text-align: left;
}
.anime-cover-image {
  border-radius: 5px;
  max-width: 196px;
  max-height: 270px;
  width: -webkit-fill-available;
}
.anime-cover-image:hover {
  transition: 0.4s ease-out;
  opacity: 0.8;
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
