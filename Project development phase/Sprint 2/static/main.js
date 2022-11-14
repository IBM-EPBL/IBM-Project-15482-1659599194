// <!-- nav bar scripts -->
    // grab everything we need
    const btn = document.querySelector('button.mobile-menu-button');
    const menu = document.querySelector(".mobile-menu");
    const btnclose = document.querySelector(".btnclose")

    // add event listener
    btn.addEventListener("click", () => {
        menu.classList.remove("hidden");
    });
    btnclose.addEventListener("click",()=>{
        menu.classList.add("hidden");
    })
// <!-- nav bar end -->


//type script animayion start
var typed = new Typed('.element', {
    strings: ["ReactJs Developer","AngularJs Developer","Node Js Developer","Data Scienetist","IOT Engineer","Machine Learning", "iOS Developer", "Android Developer", "Python Developer", "Java Developer", "UX Designer", "Virtual Reality", "Argument Developer",
    "Golang Developer","Data Analytics","AWS Engineer","Artifical Engineer"],
    typeSpeed: 60,backSpeed:60,
    loop: true
  });
// type script end