document.addEventListener("DOMContentLoaded", function () {
    const chicken = document.getElementById("chicken");

    chicken.addEventListener("mouseover", function () {
        chicken.querySelector(".wing").style.transform = "rotate(20deg)";
    });

    chicken.addEventListener("mouseout", function () {
        chicken.querySelector(".wing").style.transform = "rotate(0)";
    });
});
