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
    updateUserInput(state, userInput) {
      state.userInput = userInput;
    },
    updateAnimesData(state, animesData) {
      state.animesData = animesData;
    }
  },
  actions: {
    updateUser(context, user) {
      context.commit("updateUser", user);
    },
    updateUserInput(context, userInput) {
      context.commit("updateUserInput", userInput);
    },
    updateAnimesData(context, animesData) {
      context.commit("updateAnimesData", animesData);
    }
  },
})
