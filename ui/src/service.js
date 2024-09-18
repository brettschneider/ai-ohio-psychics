export const login = async (username, password) => {
    const response = await fetch("/api/login", {
        method: "POST",
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify({ username, password })
    });
    if (!response.ok) {
        throw new Error('Failed to log in')
    }
    return await response.json();
};

export const chat = async (token, query) => {
    const response = await fetch("/api/chat", {
        method: "POST",
        header: { "x-token": token },
        body: JSON.stringify({ query })
    })
    if (!response.ok) {
        throw new Error('Failed to log in')
    }
    return await response.json();
};