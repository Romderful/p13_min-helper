import { createStore } from 'vuex'

export default createStore({
  state: {
    user: null,
    animes_data: null,
    user_input: "",
  },
  getters: {
    getUser: (state) => {
      return state.user;
    },
    getUserInput: (state) => {
      return state.user_input
    },
    getAnimesData: (state) => {
      return state.animes_data
    }
  },
  mutations: {
    updateUser(state, user) {
      state.user = user;
    },
    updateUserInput(state, user_input) {
      state.user_input = user_input;
    },
    updateAnimesData(state, animes_data) {
      state.animes_data = animes_data;
    }
  },
  actions: {
    updateUser(context, user) {
      context.commit("updateUser", user);
    },
    updateUserInput(context, user_input) {
      context.commit("updateUserInput", user_input);
    },
    updateAnimesData(context, animes_data) {
      context.commit("updateAnimesData", animes_data);
    }
  },
})
