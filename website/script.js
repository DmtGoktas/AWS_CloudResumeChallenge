document.addEventListener("DOMContentLoaded", async () => {
    const counter = document.getElementById("count");

    if (!counter) return;

    try {
        const response = await fetch(
            "https://hfs1j4zek7.execute-api.eu-north-1.amazonaws.com/count"
        );

        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
        }

        const data = await response.json();
        counter.textContent = data.count;
    } catch (error) {
        console.error("Visitor counter error:", error);
        counter.textContent = "Unavailable";
    }
});