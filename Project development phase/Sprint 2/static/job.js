let searchEl = document.getElementById("searchBtn")
let alertBorder = document.getElementById("alertBorder")
let alertBorderClose = document.getElementById("alertBorderClose")
searchEl.addEventListener("click", () => {
    event.preventDefault();
    alertBorder.classList.remove("hidden")
})

alertBorderClose.addEventListener("click", () => {
    alertBorder.classList.add("hidden")
})

