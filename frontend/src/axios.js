import axios from "axios";


axios.defaults.baseURL = "/";

axios.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem("access_token")
        if (token && config.url !== "api-v1/auth/login/" && config.url !== "api-v1/auth/token/refresh/") {
            config.headers["Authorization"] = 'Bearer ' + token;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

axios.interceptors.response.use(
    (res) => {
        return res;
    },
    async (err) => {

        const originalConfig = err.config;
        if (originalConfig.url === "api-v1/auth/login/" || !err.response) {
            return Promise.reject(err)
        }

        if (err.response.status !== 401 || originalConfig.url === "api-v1/auth/token/refresh/") {
            return Promise.reject(err)
        }

        originalConfig._retry = true;

        try {
            const response = await axios.post("api-v1/auth/token/refresh/", {
                refresh: localStorage.getItem("refresh_token")
            });
            const {
                access
            } = response.data;
            localStorage.setItem("access_token", access)
            err.config.headers[
                "Authorization"
            ] = `Bearer ${access}`;
            return new Promise((resolve, reject) => {
                axios.request(originalConfig).then(response => {
                    resolve(response);
                }).catch((err) => {
                    reject(err);
                })
            });
        } catch (_error) {
            return Promise.reject(_error);
        }
    }
);
