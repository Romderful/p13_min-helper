<template>
  <div class="container animes">
    <div class="container mb-4">
      <h1>Home</h1>
      <br />
    </div>
    <div class="container mb-3" v-for="anime in animes" :key="anime.id">
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
  </div>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";

export default {
  name: "Home",
  data() {
    return {
      animes: null,
    };
  },
  computed: {
    ...mapGetters(["user"]),
  },
  async created() {
    const response = await axios.get("api-v1/animes/", {
      headers: {
        Authorization: "Bearer " + localStorage.getItem("access_token"),
      },
    });
    this.animes = response.data.results;
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