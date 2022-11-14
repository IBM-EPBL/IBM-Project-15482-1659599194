// grab everything we need
let profileEl = document.getElementById("profile")
let formEl = document.getElementById("profile-form")
let editEl = document.getElementById("editBtn")

editEl.addEventListener("click", () => {
    profileEl.classList.add("hidden");
    formEl.classList.remove("hidden");
})