import { createStore } from 'vuex'

export default createStore({
  state: {
    user: null,
    animesData: null,
    userInput: "",
  },
  getters: {
    getUser: (state) => {
      return state.user;
    },
    getUserInput: (state) => {
      return state.userInput
    },
    getAnimesData: (state) => {
      return state.animesData
    }
  },
  mutations: {
    updateUser(state, user) {
      state.user = user;
    },
    updateUserInput(state, user_input) {
      state.user_input = user_input;
    },
    updateAnimesData(state, animesData) {
      state.animesData = animesData;
    }
  },
  actions: {
    updateUser(context, user) {
      context.commit("updateUser", user);
    },
    updateUserInput(context, user_input) {
      context.commit("updateUserInput", user_input);
    },
    updateAnimesData(context, animesData) {
      context.commit("updateAnimesData", animesData);
    }
  },
})
