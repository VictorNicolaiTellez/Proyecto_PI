
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



//carrusel
let indice = 0;

// Supón que esto es el array de canciones que obtuviste del backend.
const cancionesBackend = [
  { id: 1, titulo: "Canción 1" },
  { id: 2, titulo: "Canción 2" },
  { id: 3, titulo: "Canción 3" },
  { id: 4, titulo: "Canción 4" },
  // Agrega más canciones según lo necesites
];

// Imagen que se va a repetir (ahora en la carpeta 'images')
const imagenCarrusel = "images/deafault_img.png"; // Ruta de la imagen en tu carpeta

// Función para cargar las imágenes repetidas según el número de canciones
function cargarImagenes() {
  const contenedor = document.querySelector('.imagenes');
  contenedor.innerHTML = ""; // Limpiar el contenedor antes de agregar las imágenes

  // Crear una imagen por cada canción en el array
  cancionesBackend.forEach(() => {
    const imgElement = document.createElement('img');
    imgElement.src = imagenCarrusel;
    imgElement.alt = 'Imagen del Carrusel';
    contenedor.appendChild(imgElement);
  });
}

// Función para mover el carrusel
function moverCarrusel(direccion) {
  const imagenes = document.querySelector('.imagenes');
  const totalImagenes = imagenes.children.length;

  indice += direccion;

  if (indice < 0) {
    indice = totalImagenes - 1;
  } else if (indice >= totalImagenes) {
    indice = 0;
  }
  imagenes.style.transform = `translateX(-${indice * 800}px)`;
}

// Llamamos a cargarImagenes cuando la página se carga
window.onload = cargarImagenes;

// Opcional: Mover el carrusel automáticamente cada 3 segundos
setInterval(() => {
  moverCarrusel(1);
}, 3000);
