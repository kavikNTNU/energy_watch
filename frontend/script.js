console.log("Energy Watch frontend is connected!");

const API_URL = "/api/components"

async function loadComponents() {
    const response = await fetch(API_URL);
    const components = await response.json();
    console.log(components)
    renderComponents(components);
}

function renderComponents(components) {
    const list = document.getElementById("component_list");
    for (const component of components) {
        const item = document.createElement("li");
        item.textContent = `${component.name} (${component.type}) - ${component.status}`;
        list.appendChild(item);
    }
}

loadComponents();