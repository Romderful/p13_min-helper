import { createStore } from 'vuex'

export default createStore({
  state: {
    user: null,
    animes_data: null,
  },
  getters: {
    getUser: (state) => {
      return state.user;
    },
    getAnimesData: (state) => {
      return state.animes_data
    }
  },
  mutations: {
    updateUser(state, user) {
      state.user = user;
    },
    updateAnimesData(state, animes_data) {
      state.animes_data = animes_data;
    }
  },
  actions: {
    updateUser(context, user) {
      context.commit("updateUser", user);
    },
    updateAnimesData(context, animes_data) {
      context.commit("updateAnimesData", animes_data);
    }
  },
})
