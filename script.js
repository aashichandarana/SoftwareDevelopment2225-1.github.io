// Typewriter Effect for Title
const title = document.getElementById("title");
const text = "Sustainable Future";
let index = 0;

function typeWriter() {
    if (index < text.length) {
        title.innerHTML += text.charAt(index);
        index++;
        setTimeout(typeWriter, 100);
    }
}

// Clear the title first, then start the typewriter effect
title.innerHTML = "";
setTimeout(typeWriter, 500);

// Button Hover Effect
const button = document.querySelector(".cta");

button.addEventListener("mouseover", () => {
    button.style.boxShadow = "0px 0px 20px rgba(26, 188, 156, 0.8)";
});

button.addEventListener("mouseleave", () => {
    button.style.boxShadow = "none";
});

// "Learn More" Button Click Alert
function learnMore() {
    alert("Learn more about sustainable agriculture and its impact!");
}
