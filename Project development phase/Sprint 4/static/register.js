let close = document.getElementById("close")
let alert = document.getElementById("alert")

function hide(params) {
    alert.classList.add("hidden");
}

setTimeout(()=>{alert.classList.add("hidden");}, 2000);

close.addEventListener("click", () => {
    hide();
})

