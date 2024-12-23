// Título animado con efecto de "escritura"
const titles = ["Bienvenido a mi Portfolio!", "Explora mis Proyectos 🚀", "Contáctame 📧"];
let index = 0;
let charIndex = 0;
let direction = 1;

function animateTitle() {
    const currentTitle = titles[index];
    document.title = currentTitle.substring(0, charIndex);
    
    // Avanza o retrocede la cantidad de caracteres
    charIndex += direction;

    // Cambio de dirección cuando termina de escribir/borrar
    if (charIndex > currentTitle.length) {
        direction = -1;
        setTimeout(() => {}, 1000); // Pausa al final de la animación
    } else if (charIndex === 0) {
        direction = 1;
        index = (index + 1) % titles.length; // Pasa al siguiente título
    }

    setTimeout(animateTitle, 200); // Velocidad de la animación
}

document.addEventListener("DOMContentLoaded", animateTitle);