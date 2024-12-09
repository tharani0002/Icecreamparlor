
const API_BASE = "http://127.0.0.1:5000";

async function fetchFlavors() {
    try {
        const response = await fetch(`${API_BASE}/flavors`);
        const flavors = await response.json();

        const flavorsDiv = document.getElementById('flavors');
        flavorsDiv.innerHTML = "";

        flavors.forEach(flavor => {
            const flavorDiv = document.createElement('div');
            flavorDiv.className = "flavor";
            flavorDiv.innerHTML = `
                <h2>${flavor.name}</h2>
                <p>${flavor.description}</p>
                <p>Status: ${flavor.availability}</p>
            `;
            flavorsDiv.appendChild(flavorDiv);
        });
    } catch (error) {
        console.error("Error fetching flavors:", error);
        const flavorsDiv = document.getElementById('flavors');
        flavorsDiv.innerHTML = "<p>Failed to load flavors. Please try again later.</p>";
    }
}
