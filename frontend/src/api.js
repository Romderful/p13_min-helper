import axios from "axios"


async function getData(url) {
    const data = await axios.get(url, {
        headers: {
            Authorization: "Bearer " + localStorage.getItem("access_token"),
        },
    });
    return data;
}


export { getData };