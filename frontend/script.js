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
    list.replaceChildren();
    for (const component of components) {
        const item = document.createElement("li");
        item.textContent = `${component.name} (${component.type}) - ${component.status}`;
        list.appendChild(item);
    }
}

const form = document.getElementById("component-form");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const formData = new FormData(form);
  const component = {
    name: formData.get("name"),
    status: formData.get("status"),
    type: formData.get("type"),
  };

  const response = await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(component),
  });

  if (!response.ok) {
    alert("Failed to add component. Please try again.");
    return;
  }

  form.reset();
  loadComponents();
});

loadComponents();