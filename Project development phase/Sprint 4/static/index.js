let goEl = document.getElementById("go")
let searchAlert = document.getElementById("defaultModal");
let closeBtn = document.getElementById("closebtn");

goEl.addEventListener("click", () => {
    event.preventDefault();
    searchAlert.classList.remove("hidden");
})

closeBtn.addEventListener("click",()=>     searchAlert.classList.add("hidden"))