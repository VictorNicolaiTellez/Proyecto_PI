console.log("JS cargado correctamente");

document.addEventListener("DOMContentLoaded", () => {
    const carrusel = document.querySelector('.carousel_index');
    const card = document.querySelector('.music-card_index');
    const cardWidth = card ? card.offsetWidth + 10 : 260;

    function moverCarrusel(direccion) {
        if (carrusel) {
            carrusel.scrollLeft += direccion * cardWidth * 2;
        }
    }

    document.querySelector('.prev-btn_index').addEventListener('click', () => moverCarrusel(-1));
    document.querySelector('.next-btn_index').addEventListener('click', () => moverCarrusel(1));

});
