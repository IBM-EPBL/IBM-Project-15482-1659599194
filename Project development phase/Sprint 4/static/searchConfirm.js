// prompt for go button want to user confirm pressing the search button
let promptBox = document.getElementById("popup-modal");
let goButton = document.getElementById("goButton");
let promptCancel = document.getElementById("cancelBtn");
let promptClose = document.getElementById("promptClose");
let confirmSearch = document.getElementById("confirmSearch");

goButton.addEventListener("click", () => {
    event.preventDefault();
    promptBox.classList.remove("hidden");
})

promptCancel.addEventListener("click", () => promptBox.classList.add("hidden"));
promptClose.addEventListener("click", () => promptBox.classList.add("hidden"));
confirmSearch.addEventListener("click",()=> document.getElementById("form-1").submit())