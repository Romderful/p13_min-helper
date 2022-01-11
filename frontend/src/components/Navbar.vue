<template>
  <div class="container">
    <nav class="py-2 bg-light border-bottom">
      <div class="container d-flex flex-wrap">
        <ul class="nav me-auto">
          <li class="nav-item">
            <router-link to="/"
              ><a class="nav-link link-dark px-2 active" aria-current="page"
                >Home</a
              ></router-link
            >
          </li>
          <li class="nav-item">
            <router-link to="about"
              ><a class="nav-link link-dark px-2">About</a></router-link
            >
          </li>
        </ul>
        <ul class="nav">
          <li class="nav-item">
            <router-link to="log-in"
              ><a href="#" class="nav-link link-dark px-2"
                >Login</a
              ></router-link
            >
          </li>
          <li class="nav-item">
            <router-link to="sign-up"
              ><a href="#" class="nav-link link-dark px-2"
                >Sign up</a
              ></router-link
            >
          </li>
        </ul>
      </div>
    </nav>
    <header class="py-3 mb-5 border-bottom">
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
        <form class="col-12 col-lg-auto mb-3 mb-lg-0">
          <input
            type="search"
            class="form-control"
            placeholder="Search..."
            aria-label="Search"
          />
        </form>
      </div>
    </header>
  </div>
</template>

<style>
.b-example-divider {
  height: 3rem;
  background-color: rgba(0, 0, 0, 0.1);
  border: solid rgba(0, 0, 0, 0.15);
  border-width: 1px 0;
  box-shadow: inset 0 0.5em 1.5em rgba(0, 0, 0, 0.1),
    inset 0 0.125em 0.5em rgba(0, 0, 0, 0.15);
}

.form-control-dark {
  color: #fff;
  background-color: var(--bs-dark);
  border-color: var(--bs-gray);
}
.form-control-dark:focus {
  color: #fff;
  background-color: var(--bs-dark);
  border-color: #fff;
  box-shadow: 0 0 0 0.25rem rgba(255, 255, 255, 0.25);
}

.bi {
  vertical-align: -0.125em;
  fill: currentColor;
}

.text-small {
  font-size: 85%;
}

.dropdown-toggle {
  outline: 0;
}
</style>