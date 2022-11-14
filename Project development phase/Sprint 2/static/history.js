let historyErrorBtn = document.getElementById("historyErrorBtn")
let historyErrorEl = document.getElementById("historyError")

historyErrorBtn.addEventListener("click", () => {
    historyErrorEl.classList.add("hidden");
})

setTimeout(()=>{historyErrorEl.classList.add("hidden");}, 3000);