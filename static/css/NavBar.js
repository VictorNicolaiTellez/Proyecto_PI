
document.addEventListener("DOMContentLoaded", function () {
    console.log("El script está funcionando");
    
    let currentPath = window.location.pathname; // Obtiene la ruta completa, ejemplo: "/songs/"
    console.log("Ruta actual:", currentPath);

    let links = document.querySelectorAll(".nav-links li a");
    console.log("Enlaces encontrados:", links.length);

    links.forEach(link => {
        let linkPath = link.getAttribute("href"); // Obtiene la ruta del enlace
        console.log("Revisando:", linkPath);

        // Si la ruta del enlace coincide con la ruta actual, activa el enlace
        if (currentPath === linkPath) {
            link.parentElement.classList.add("active");
            console.log("Clase 'active' añadida a:", link.textContent);
        }
    });
});

