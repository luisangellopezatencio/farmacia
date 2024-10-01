

const URL_API = import.meta.env.VITE_URL_API + "/login";

class apiAdapter {
    async login(username: string, password: string) {
        const response = await fetch(URL_API, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ username, password }),
        });