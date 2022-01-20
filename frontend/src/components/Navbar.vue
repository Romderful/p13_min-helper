<template>
  <div class="container fixed-top">
    <nav
      class="main-navbar navbar-expand-lg navbar-light bg-light border-bottom"
    >
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="true"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div
        class="collapse navbar-collapse container"
        id="navbarSupportedContent"
      >
        <ul class="nav me-auto">
          <li class="nav-item col-12 col-lg-auto">
            <router-link to="/" class="nav-link link-dark px-2 active"
              >Home</router-link
            >
          </li>
          <li class="nav-item col-12 col-lg-auto">
            <router-link to="about" class="nav-link link-dark px-2"
              >About</router-link
            >
          </li>
        </ul>
        <ul v-if="!user" class="nav auth">
          <li class="nav-item col-12 col-lg-auto">
            <router-link to="log-in" class="nav-link link-dark px-2"
              >Login</router-link
            >
          </li>
          <li class="nav-item col-12 col-lg-auto">
            <router-link to="sign-up" class="nav-link link-dark px-2"
              >Sign up</router-link
            >
          </li>
        </ul>
        <ul v-if="user" class="nav auth">
          <li class="nav-item col-12 col-lg-auto">
            <a
              href="javascript:void(0)"
              @click="handleClick"
              class="nav-link link-dark px-2"
              >Logout</a
            >
          </li>
        </ul>
        <form class="col-12 col-lg-auto mb-3 mb-lg-0">
          <input
            type="search"
            class="form-control"
            placeholder="Search..."
            aria-label="Search"
          />
        </form>
      </div>
    </nav>
    <header class="py-3 mb-5 bg-white border-bottom">
      <div class="container d-flex flex-wrap justify-content-center">
        <a
          href="/"
          class="
            d-flex
            align-items-center
            mb-3 mb-lg-0
            me-lg-auto
            text-dark text-decoration-none
          "
        >
          <h1 class="text-center">min-helper</h1>
        </a>
      </div>
    </header>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Navbar",
  methods: {
    handleClick() {
      localStorage.removeItem("access_token");
      this.$store.dispatch("user", null);
      this.$router.push("/");
    },
  },
  computed: {
    ...mapGetters(["user"]),
  },
};
</script>

<style>
.main-navbar {
  text-align: left;
  padding: 6px;
}
.auth {
  margin-right: 2rem;
}
</style>