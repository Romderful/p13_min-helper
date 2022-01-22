import { createStore } from 'vuex'

export default createStore({
  state: {
    user: null,
    animes_data: null,
  },
  getters: {
    user: (state) => {
      return state.user;
    },
    animes_data: (state) => {
      return state.animes_data
    }
  },
  mutations: {
    user(state, user) {
      state.user = user;
    },
    animes_data(state, animes_data) {
      state.animes_data = animes_data;
    }
  },
  actions: {
    user(context, user) {
      context.commit("user", user);
    },
    animes_data(context, animes_data) {
      context.commit("animes_data", animes_data);
    }
  },
})
