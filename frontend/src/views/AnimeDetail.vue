<template>
  <div
    v-if="animeData.description"
    v-html="animeData.description"
    class="container"
  ></div>
  <div v-else class="container">
    <p>We're sorry, the description isn't available yet.</p>
  </div>
  <div class="container animes-wrapper">
    <div class="row mb-3">
      <transition-group name="fade" appear>
        <div
          class="container mb-3 col-6 col-lg-2"
          v-for="anime in linkedAnimesData"
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
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import { getData } from "../api";

export default {
  name: "AnimeDetail",
  props: ["id"],
  watch: {
    async $route() {
      if (this.$route.name !== "AnimeDetail") {
        return;
      }
      this.linkedAnimesData = [];
      const response = await getData(`api-v1/animes/${this.$route.params.id}/`);
      this.animeData = response.data;
      let linkedAnimesId = Object.values(this.animeData.linked_animes);
      for (const id of linkedAnimesId) {
        this.getLinkedAnimes(id);
      }
      window.scrollTo({ top: 0, behavior: "smooth" });
    },
  },
  data() {
    return {
      animeData: "",
      linkedAnimesData: [],
    };
  },
  methods: {
    async getLinkedAnimes(id) {
      const response = await getData(`api-v1/animes/${id}/`);
      this.linkedAnimesData.push(response.data);
    },
  },
  computed: {
    ...mapGetters(["getAnimesData"]),
  },
  async created() {
    const response = await getData(`api-v1/animes/${this.id}/`);
    this.animeData = response.data;
    let linkedAnimesId = Object.values(this.animeData.linked_animes);
    for (const id of linkedAnimesId) {
      this.getLinkedAnimes(id);
    }
  },
};
</script>