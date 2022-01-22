import axios from "axios"

async function getPage(page_number) {
    const data = await axios.get(`api-v1/animes/?page=${page_number}`, {
        headers: {
            Authorization: "Bearer " + localStorage.getItem("access_token"),
        },
    });
    return data;
}

export { getPage };