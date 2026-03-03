// Dark / Light Mode Toggle
const toggle = document.getElementById("themeToggle");

toggle.addEventListener("click", () => {
    document.body.classList.toggle("light-mode");
    toggle.textContent = 
        document.body.classList.contains("light-mode") ? "🌙" : "☀";
});

// Typing Animation
window.onload = function () {
    const typingElement = document.getElementById("typingEffect");
    if (!typingElement) return;

    const text = typingElement.textContent;
    typingElement.textContent = "";
    let i = 0;

    function type() {
        if (i < text.length) {
            typingElement.textContent += text.charAt(i);
            i++;
            setTimeout(type, 20);
        }
    }

    type();
};

// Simple Background Animation
const particles = document.getElementById("particles");
for (let i = 0; i < 40; i++) {
    let dot = document.createElement("div");
    dot.style.position = "absolute";
    dot.style.width = "4px";
    dot.style.height = "4px";
    dot.style.background = "white";
    dot.style.borderRadius = "50%";
    dot.style.top = Math.random() * 100 + "vh";
    dot.style.left = Math.random() * 100 + "vw";
    dot.style.opacity = Math.random();
    particles.appendChild(dot);
}