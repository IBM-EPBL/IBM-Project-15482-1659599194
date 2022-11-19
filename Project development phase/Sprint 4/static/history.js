// active pagination button
let btn0 = document.getElementById("btn-0")
let btn1 = document.getElementById("btn-1")
let btn2 = document.getElementById("btn-2")

let Npath = window.location.pathname
if (Npath.split("/")[2] == 0)
    btn0.classList.add("!bg-purple-300")
else if (Npath.split("/")[2] == 1)
    btn1.classList.add("!bg-purple-300")
else if (Npath.split("/")[2] == 2)
    btn2.classList.add("!bg-purple-300")

// history page button shows error
let historyErrorBtn = document.getElementById("historyErrorBtn")
let historyErrorEl = document.getElementById("historyError")

historyErrorBtn.addEventListener("click", () => {
    historyErrorEl.classList.add("hidden");
})

setTimeout(() => { historyErrorEl.classList.add("hidden"); }, 3000);

