document.addEventListener("DOMContentLoaded", function () {
    const carruseles = document.querySelectorAll(".carousel_index"); // Obtiene todos los carruseles

    function moverCarrusel(direccion, indice) {
        const carrusel = carruseles[indice]; // Selecciona el carrusel correcto
        if (!carrusel) return;

        const desplazamiento = carrusel.offsetWidth + 10; // Tamaño de desplazamiento con espacio
        carrusel.scrollBy({ left: direccion * desplazamiento, behavior: "smooth" }); // Desplazamiento suave
    }

    // Para cada botón, aseguramos que tenga su evento correspondiente
    document.querySelectorAll(".prev-btn_index").forEach((btn, index) => {
        btn.addEventListener("click", () => moverCarrusel(-1, index));
    });

    document.querySelectorAll(".next-btn_index").forEach((btn, index) => {
        btn.addEventListener("click", () => moverCarrusel(1, index));
    });
});
