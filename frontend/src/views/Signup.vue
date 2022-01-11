<template>
  <main class="form-signup">
    <form v-if="successRegister == false" @submit.prevent="handleSubmit">
      <h1 class="h3 mb-3 fw-normal">Please sign up</h1>
      <div v-if="errors.username" class="alert alert-danger" role="alert">
        <p>{{ errors.username[0] }}</p>
      </div>
      <div class="form-floating">
        <input
          type="text"
          class="form-control"
          placeholder="username"
          v-model="username"
        />
        <label for="floatingInput">Username</label>
      </div>
      <div v-if="errors.email" class="alert alert-danger mt-3" role="alert">
        <p>{{ errors.email[0] }}</p>
      </div>
      <div class="form-floating">
        <input
          type="email"
          class="form-control"
          placeholder="name@example.com"
          v-model="email"
        />
        <label for="floatingInput">Email address</label>
      </div>
      <div
        v-if="errors.non_field_errors"
        class="alert alert-danger mt-3"
        role="alert"
      >
        <p>{{ errors.non_field_errors[0] }}</p>
      </div>
      <div v-if="errors.password1" class="alert alert-danger mt-3" role="alert">
        <p>{{ errors.password1[0] }}</p>
      </div>
      <div class="form-floating">
        <input
          type="password"
          class="form-control"
          id="floatingPassword"
          placeholder="Password"
          v-model="password1"
        />
        <label for="floatingPassword">Password</label>
      </div>
      <div v-if="errors.password2" class="alert alert-danger mt-3" role="alert">
        <p>{{ errors.password2[0] }}</p>
      </div>
      <div class="form-floating">
        <input
          type="password"
          class="form-control"
          id="floatingPassword1"
          placeholder="Password confirmation"
          v-model="password2"
        />
        <label for="floatingPassword">Password confirmation</label>
      </div>

      <button class="w-100 btn btn-lg btn-primary" type="submit">
        Sign up
      </button>
      <p class="mt-5 mb-3 text-muted">&copy; 2022</p>
    </form>
    <div v-else class="alert alert-success" role="alert">
      You have been registered !
      <br />
      <p>
        You can now go to the <router-link to="log-in">login page</router-link>
      </p>
    </div>
  </main>
</template>

<script>
import axios from "axios";

export default {
  name: "Signup",
  data() {
    return {
      username: "",
      email: "",
      password1: "",
      password2: "",
      successRegister: false,
      errors: "",
    };
  },
  methods: {
    async handleSubmit() {
      try {
        const response = await axios.post("api-v1/auth/registration/", {
          username: this.username,
          email: this.email,
          password1: this.password1,
          password2: this.password2,
        });
        if (response.status == 201) {
          this.successRegister = true;
        }
      } catch (e) {
        this.errors = e.response.data;
      }
    },
  },
};
</script>

<style>
.form-signup {
  max-width: 330px;
  padding: 15px;
  margin: auto;
}

.form-signup .form-floating:focus-within {
  z-index: 2;
}

.form-signup input[type="text"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.form-signup input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.form-signup input[type="password"] {
  margin-bottom: -1px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}

#floatingPassword1 {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
</style>