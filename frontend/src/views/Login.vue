<template>
  <main class="form-signin">
    <form @submit.prevent="handleSubmit">
      <h1 class="h3 mb-3 fw-normal">Please sign in</h1>
      <div
        v-if="errors.non_field_errors"
        class="alert alert-danger mt-3"
        role="alert"
      >
        <p>{{ errors.non_field_errors[0] }}</p>
      </div>
      <div class="form-floating">
        <input
          type="email"
          class="form-control"
          id="floatingInput"
          placeholder="name@example.com"
          v-model="email"
        />
        <label for="floatingInput">Email address</label>
      </div>
      <div v-if="errors.password" class="alert alert-danger mt-3" role="alert">
        <p>{{ errors.password[0] }}</p>
      </div>
      <div class="form-floating">
        <input
          type="password"
          class="form-control"
          id="floatingPassword"
          placeholder="Password"
          v-model="password"
        />
        <label for="floatingPassword">Password</label>
      </div>

      <div class="checkbox mb-3">
        <label>
          <input type="checkbox" value="remember-me" /> Remember me
        </label>
      </div>
      <button class="w-100 btn btn-lg btn-primary" type="submit">
        Sign in
      </button>
      <p class="mt-5 mb-3 text-muted">&copy; 2022</p>
    </form>
  </main>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      email: "",
      password: "",
      errors: "",
    };
  },
  methods: {
    async handleSubmit() {
      try {
        const response = await axios.post("api-v1/auth/login/", {
          email: this.email,
          password: this.password,
        });
        if (response.status == 200) {
          localStorage.setItem("access_token", response.data.access_token);
          this.$store.dispatch("user", response.data.user);
          this.$router.push("/");
        }
      } catch (e) {
        this.errors = e.response.data;
      }
    },
  },
};
</script>

<style>
.form-signin {
  max-width: 330px;
  padding: 15px;
  margin: auto;
  margin-bottom: 7rem;
  margin-top: 15rem;
}

.form-signin .checkbox {
  font-weight: 400;
}

.form-signin .form-floating:focus-within {
  z-index: 2;
}

.form-signin input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
</style>