<template>
  <div class="container favourites">
    <div class="row">
      <div
        class="mb-3 col-6 col-lg-2"
        v-for="anime in getAnimesData.results"
        :key="anime.id"
      >
        <div v-if="anime.anime_details" class="anime-card card border-0">
          <div v-if="anime.anime_details.is_favourite">
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
                @click="deleteFavourite(anime.id)"
                xmlns="http://www.w3.org/2000/svg"
                width="25"
                height="25"
                fill="currentColor"
                class="bi bi-trash2-fill"
                viewBox="0 0 16 16"
              >
                <path
                  d="M2.037 3.225A.703.703 0 0 1 2 3c0-1.105 2.686-2 6-2s6 .895 6 2a.702.702 0 0 1-.037.225l-1.684 10.104A2 2 0 0 1 10.305 15H5.694a2 2 0 0 1-1.973-1.671L2.037 3.225zm9.89-.69C10.966 2.214 9.578 2 8 2c-1.58 0-2.968.215-3.926.534-.477.16-.795.327-.975.466.18.14.498.307.975.466C5.032 3.786 6.42 4 8 4s2.967-.215 3.926-.534c.477-.16.795-.327.975-.466-.18-.14-.498-.307-.975-.466z"
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

  methods: {
    async deleteFavourite(anime_id) {
      if (confirm("Do you really want to delete this favourite ?")) {
        await axios.delete(`api-v1/animes-favourites/${anime_id}/`);
        this.setAnimesData();
      }
    },

    async setAnimesData() {
      const response = await axios.get(
        `api-v1/animes-favourites/?user=${this.getUser.username}`
      );
      this.$store.dispatch("updateAnimesData", response.data);
    },
  },

  created() {
    this.setAnimesData();
  },
};
</script>

<style>
.favourites {
  margin-bottom: 7rem;
  margin-top: 15rem;
}
.bi-trash2-fill {
  position: absolute;
  right: 0;
  margin-top: -0.6rem;
  margin-right: -0.6rem;
}
.bi-trash2-fill:hover {
  transition: all 0.4s ease;
  transform: scale(1.5);
  color: red;
}
</style>