console.log("Energy Watch frontend is connected!");

const API_URL = "/api/components"

async function loadComponents() {
    const response = await fetch(API_URL);
    const components = await response.json();
    console.log(components)
}

loadComponents();