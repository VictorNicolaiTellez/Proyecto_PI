-- Tabla de Users
CREATE TABLE Users (
    username TEXT PRIMARY KEY,
    fullname TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    user_type TEXT CHECK(user_type IN ('artist', 'customer', 'admin')) NOT NULL,
    password_hash TEXT NOT NULL,
    signup_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de Artists (extiende Users)
CREATE TABLE Artists (
    artist_username TEXT PRIMARY KEY,
    artist_name TEXT NOT NULL,
    biography TEXT,
    profile_image TEXT,
    FOREIGN KEY (artist_username) REFERENCES Users(username)
);

-- Tabla de Albums
CREATE TABLE Albums (
    album_id INTEGER PRIMARY KEY AUTOINCREMENT,
    artist TEXT NOT NULL,
    title TEXT NOT NULL,
    launch_date DATE NOT NULL,
    cover TEXT,
    price DECIMAL(5,2),
    FOREIGN KEY (artist) REFERENCES Artists(artist_username)
);

-- Tabla de Songs
CREATE TABLE Songs (
    song_id INTEGER PRIMARY KEY AUTOINCREMENT,
    artist TEXT NOT NULL,
    album INTEGER NOT NULL,
    title TEXT NOT NULL,
    duration TIME NOT NULL,
    audio_file TEXT NOT NULL,
    price DECIMAL(5,2),
    FOREIGN KEY (artist) REFERENCES Artists(artist_username),
    FOREIGN KEY (album) REFERENCES Albums(album_id)
);

CREATE TABLE Vinyls (
    vinyl_id INTEGER PRIMARY KEY AUTOINCREMENT,
    price DECIMAL(5,2)
);

CREATE TABLE CDs (
    cd_id INTEGER PRIMARY KEY AUTOINCREMENT,
    price DECIMAL(5,2)
);

CREATE TABLE Merchandising (
    merchandising_id INTEGER PRIMARY KEY AUTOINCREMENT,
    merchandising_type TEXT NOT NULL,
    price DECIMAL(5,2)
);

-- Tabla de Purchases
CREATE TABLE Purchases (
    purchase_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    album INTEGER,
    song INTEGER,
    purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    monto_total DECIMAL(5,2) NOT NULL,
    FOREIGN KEY (user) REFERENCES Users(username),
    FOREIGN KEY (album) REFERENCES Albums(album_id),
    FOREIGN KEY (song) REFERENCES Songs(song_id)
);

-- Tabla de Reproducciones
CREATE TABLE Plays (
    play_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    song INTEGER NOT NULL,
    play_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (username) REFERENCES Users(username),
    FOREIGN KEY (song) REFERENCES Songs(song_id)
);

-- Insertar datos de prueba en Usuarios
INSERT INTO usuarios (nombre, email, tipo_usuario, contraseña_hash) VALUES
('Carlos Pérez', 'carlos@example.com', 'artista', 'hash123'),
('María Gómez', 'maria@example.com', 'comprador', 'hash456'),
('Admin', 'admin@example.com', 'admin', 'hash789');

-- Insertar datos de prueba en Artistas
INSERT INTO artistas (id_artista, nombre_artístico, biografía, imagen_perfil) VALUES
(1, 'Los Rockeros', 'Banda de rock independiente', 'rockeros.jpg');

-- Insertar datos de prueba en Álbumes
INSERT INTO albumes (id_artista, titulo, fecha_lanzamiento, portada, precio) VALUES
(1, 'Rock en Vivo', '2023-08-15', 'rockenvivo.jpg', 9.99);

-- Insertar datos de prueba en Canciones
INSERT INTO canciones (id_album, titulo, duración, archivo_audio, precio) VALUES
(1, 'Canción 1', '00:03:45', 'cancion1.mp3', 1.29),
(1, 'Canción 2', '00:04:10', 'cancion2.mp3', 1.29);

-- Insertar una compra de prueba
INSERT INTO compras (id_usuario, id_album, fecha_compra, monto_total) VALUES
(2, 1, CURRENT_TIMESTAMP, 9.99);

-- Insertar una reproducción de prueba
INSERT INTO reproducciones (id_usuario, id_cancion, fecha_hora) VALUES
(2, 1, CURRENT_TIMESTAMP);


