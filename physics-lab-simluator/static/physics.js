
const userInput = document.getElementById("userInput");
const results = document.getElementById("results");

userInput.addEventListener("submit", async function(event) {
    event.preventDefault();

    const velocity = document.getElementById("initial_velocity").value;
    const angle = document.getElementById("launch_angle").value;
    const time = document.getElementById("total_time").value;

    const response = await fetch("/simulate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            velocity: velocity,
            angle: angle,
            time: time
        })
    });
    const data = await response.json();

    results.classList.remove("hidden");

    document.getElementById("max_height").textContent = `${data.max_height.toFixed(2)} m`;
    document.getElementById("total_distance").textContent = `${data.total_distance.toFixed(2)} m`;
});