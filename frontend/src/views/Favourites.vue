<template>
  <div class="container favourites">
    <div class="row">
      <div
        class="mb-3 col-6 col-lg-2"
        v-for="anime in getAnimesData.results"
        :key="anime.id"
      >
        <div v-if="anime.anime_details" class="anime-card card border-0">
          <div class="image-wrapper card">
            <router-link
              class="router-link"
              :to="{
                name: 'AnimeDetail',
                params: { id: anime.anime_details.id },
              }"
              ><img
                class="anime-cover-image"
                :src="anime.anime_details.cover_image"
            /></router-link>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="18"
              height="18"
              :fill="anime.anime_details.is_favourite ? 'red' : 'currentColor'"
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
            :to="{
              name: 'AnimeDetail',
              params: { id: anime.anime_details.id },
            }"
          >
            <p class="anime-name">
              <strong>{{ anime.anime_details.english_name }}</strong>
            </p>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";

export default {
  name: "Favourites",

  computed: {
    ...mapGetters(["getAnimesData"]),
    ...mapGetters(["getUser"]),
  },

  async created() {
    const response = await axios.get(
      `api-v1/animes-favourites/?user=${this.getUser.username}`
    );
    this.$store.dispatch("updateAnimesData", response.data);
  },
};
</script>

<style>
.favourites {
  margin-bottom: 7rem;
  margin-top: 15rem;
}
</style>