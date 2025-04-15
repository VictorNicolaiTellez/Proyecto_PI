CREATE TABLE Users (
    username VARCHAR(50) PRIMARY KEY,
    fullname VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    user_type VARCHAR(50) CHECK(user_type IN ('artist', 'customer', 'admin')) NOT NULL,
    password_hash VARCHAR(50) NOT NULL,
    signup_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de Artists
CREATE TABLE Artists (
    artist_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    artist_name TEXT NOT NULL
);



-- Tabla de Users_Artists (extiende Users, referencia a Artists)
CREATE TABLE Users_Artists (
    artist_username VARCHAR(50) ,
    artist_id INTEGER PRIMARY KEY,
    biography TEXT,
    profile_image TEXT,
    FOREIGN KEY (artist_username) REFERENCES Users(username),
    FOREIGN KEY (artist_id) REFERENCES Artists(artist_id)
);

-- Tabla de Albums
CREATE TABLE Albums (
    album_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    artist INTEGER NOT NULL,
    title VARCHAR(100) NOT NULL,
    launch_date DATE NOT NULL,
    cover TEXT,
    price DECIMAL(5,2),
    FOREIGN KEY (artist) REFERENCES Artists(artist_id)
);
-- Tabla de Songs
CREATE TABLE Songs (
    song_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    artist INTEGER NOT NULL,
    album INTEGER NOT NULL,
    title VARCHAR(100) NOT NULL,
    duration TIME NOT NULL,
    audio_file VARCHAR(255) NOT NULL,
    price DECIMAL(5,2),
    FOREIGN KEY (artist) REFERENCES Artists(artist_id),
    FOREIGN KEY (album) REFERENCES Albums(album_id)
);

CREATE TABLE Vinyls (
    vinyl_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    price DECIMAL(5,2)
);

CREATE TABLE CDs (
    cd_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    price DECIMAL(5,2)
);

CREATE TABLE Merchandising (
    merchandising_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    merchandising_type TEXT NOT NULL,
    price DECIMAL(5,2)
);

-- Tabla de Purchases
CREATE TABLE Purchases (
    purchase_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    album INTEGER,
    song INTEGER,
    purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    monto_total DECIMAL(5,2) NOT NULL,
    FOREIGN KEY (username) REFERENCES Users(username),
    FOREIGN KEY (album) REFERENCES Albums(album_id),
    FOREIGN KEY (song) REFERENCES Songs(song_id)
);

-- Tabla de Reproducciones
CREATE TABLE Plays (
    play_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    song INTEGER NOT NULL,
    play_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (username) REFERENCES Users(username),
    FOREIGN KEY (song) REFERENCES Songs(song_id)
);

-- Tabla intermedia
CREATE TABLE artist_song (
    artist_id INT NOT NULL,
    song_id INT NOT NULL,
    PRIMARY KEY (artist_id, song_id),
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id) ON DELETE CASCADE,
    FOREIGN KEY (song_id) REFERENCES songs(song_id) ON DELETE CASCADE
);


-- Insertar datos de prueba en Usuarios
INSERT INTO Users (username, fullname, email, user_type, password_hash)
VALUES 
('artista01', 'Ana Torres', 'ana.torres@example.com', 'artist', 'hash123'),
('cliente01', 'Carlos Pérez', 'carlos.perez@example.com', 'customer', 'hash456'),
('admin01', 'Laura Gómez', 'laura.gomez@example.com', 'admin', 'hash789'),
('artista02', 'Luis Rivera', 'luis.rivera@example.com', 'artist', 'hash321'),
('cliente02', 'Sofía Díaz', 'sofia.diaz@example.com', 'customer', 'hash654');


-- Insertar datos de prueba en Artists
INSERT INTO Artists (artist_name) VALUES
('Maroon 5'),      -- id 1
('Arctic Monkeys'),-- id 2
('Green Day'),     -- id 3
('Coldplay'),      -- id 4
('John Newman'),   -- id 5
('Oasis'),         -- id 6
('Wiz Khalifa');   -- id 7

-- Insertar datos de prueba en Albums
INSERT INTO Albums (artist, title, launch_date, cover, price) VALUES
(5, 'Tribute', '2013-10-14', 'tribute.jpg', 9.99),                      -- id 1
(1, 'V', '2014-08-29', 'v.jpg', 10.99),                                 -- id 2
(4, 'A Head Full of Dreams', '2015-12-04', 'head_full_dreams.jpg', 11.99), -- id 3
(3, 'Boulevard of Broken Dreams', '2004-09-21', 'broken_dreams.jpg', 8.99), -- id 4
(1, 'Overexposed Track By Track', '2012-06-26', 'overexposed.jpg', 9.49), -- id 5
(6, '(What''s The Story) Morning Glory?', '1995-10-02', 'morning_glory.jpg', 10.50), -- id 6
(2, 'Favourite Worst Nightmare', '2007-04-23', 'fwn.jpg', 8.75);       -- id 7


-- Insertar datos de prueba en Songs
-- Álbum 1: Tribute (John Newman)
INSERT INTO Songs (artist, album, title, duration, audio_file, price) VALUES
(5, 1, 'Tribute', '00:04:10', 'tribute.mp3', 1.29),
(5, 1, 'Love Me Again', '00:04:00', 'love_me_again.mp3', 1.29),
(5, 1, 'Losing Sleep', '00:03:42', 'losing_sleep.mp3', 1.29),
(5, 1, 'Easy', '00:03:40', 'easy.mp3', 1.29),
(5, 1, 'Try', '00:03:40', 'try.mp3', 1.29),
(5, 1, 'Out of My Head', '00:03:50', 'out_of_my_head.mp3', 1.29),
(5, 1, 'Cheating', '00:03:42', 'cheating.mp3', 1.29),
(5, 1, 'Running', '00:03:40', 'running.mp3', 1.29),
(5, 1, 'Gold Dust', '00:03:40', 'gold_dust.mp3', 1.29),
(5, 1, 'Goodnight Goodbye', '00:03:40', 'goodnight_goodbye.mp3', 1.29),
(5, 1, 'All I Need Is You', '00:03:40', 'all_i_need_is_you.mp3', 1.29);
-- Álbum 2: V (Maroon 5)
INSERT INTO Songs (artist, album, title, duration, audio_file, price) VALUES
(1, 2, 'Maps', '00:03:10', 'maps.mp3', 1.29),
(1, 2, 'Animals', '00:03:51', 'animals.mp3', 1.29),
(1, 2, 'It Was Always You', '00:04:00', 'it_was_always_you.mp3', 1.29),
(1, 2, 'Unkiss Me', '00:03:58', 'unkiss_me.mp3', 1.29),
(1, 2, 'Sugar', '00:03:55', 'sugar.mp3', 1.29),
(1, 2, 'Leaving California', '00:03:23', 'leaving_california.mp3', 1.29),
(1, 2, 'In Your Pocket', '00:03:39', 'in_your_pocket.mp3', 1.29),
(1, 2, 'New Love', '00:03:16', 'new_love.mp3', 1.29),
(1, 2, 'Coming Back for You', '00:03:47', 'coming_back_for_you.mp3', 1.29),
(1, 2, 'Feelings', '00:03:14', 'feelings.mp3', 1.29),
(1, 2, 'My Heart Is Open', '00:03:57', 'my_heart_is_open.mp3', 1.29);
-- Álbum 3: A Head Full of Dreams (Coldplay)
INSERT INTO Songs (artist, album, title, duration, audio_file, price) VALUES
(4, 3, 'A Head Full of Dreams', '00:03:44', 'a_head_full_of_dreams.mp3', 1.29),
(4, 3, 'Birds', '00:03:49', 'birds.mp3', 1.29),
(4, 3, 'Hymn for the Weekend', '00:04:18', 'hymn_for_the_weekend.mp3', 1.29),
(4, 3, 'Everglow', '00:04:42', 'everglow.mp3', 1.29),
(4, 3, 'Adventure of a Lifetime', '00:04:23', 'adventure_of_a_lifetime.mp3', 1.29),
(4, 3, 'Fun', '00:04:27', 'fun.mp3', 1.29),
(4, 3, 'Kaleidoscope', '00:01:51', 'kaleidoscope.mp3', 1.29),
(4, 3, 'Army of One', '00:06:16', 'army_of_one.mp3', 1.29),
(4, 3, 'Amazing Day', '00:04:27', 'amazing_day.mp3', 1.29),
(4, 3, 'Colour Spectrum', '00:01:00', 'colour_spectrum.mp3', 1.29),
(4, 3, 'Up&Up', '00:06:45', 'up_and_up.mp3', 1.29);
-- Álbum 4: American Idiot (Green Day)
INSERT INTO Songs (artist, album, title, duration, audio_file, price) VALUES
(3, 4, 'American Idiot', '00:02:54', 'american_idiot.mp3', 1.29),
(3, 4, 'Jesus of Suburbia', '00:09:08', 'jesus_of_suburbia.mp3', 1.29),
(3, 4, 'Holiday', '00:03:52', 'holiday.mp3', 1.29),
(3, 4, 'Boulevard of Broken Dreams', '00:04:20', 'boulevard_of_broken_dreams.mp3', 1.29),
(3, 4, 'Are We the Waiting', '00:02:42', 'are_we_the_waiting.mp3', 1.29),
(3, 4, 'St. Jimmy', '00:02:55', 'st_jimmy.mp3', 1.29),
(3, 4, 'Give Me Novacaine', '00:03:25', 'give_me_novacaine.mp3', 1.29),
(3, 4, 'She’s a Rebel', '00:02:00', 'shes_a_rebel.mp3', 1.29),
(3, 4, 'Extraordinary Girl', '00:03:33', 'extraordinary_girl.mp3', 1.29),
(3, 4, 'Letterbomb', '00:04:06', 'letterbomb.mp3', 1.29),
(3, 4, 'Wake Me Up When September Ends', '00:04:45', 'wake_me_up_when_september_ends.mp3', 1.29),
(3, 4, 'Homecoming', '00:09:18', 'homecoming.mp3', 1.29),
(3, 4, 'Whatsername', '00:04:12', 'whatsername.mp3', 1.29);
-- Álbum 5: Overexposed (Maroon 5)
INSERT INTO Songs (artist, album, title, duration, audio_file, price) VALUES
(1, 5, 'One More Night', '00:03:39', 'one_more_night.mp3', 1.29),
(1, 5, 'Payphone', '00:03:51', 'payphone.mp3', 1.29),
(1, 5, 'Daylight', '00:03:46', 'daylight.mp3', 1.29),
(1, 5, 'Lucky Strike', '00:03:05', 'lucky_strike.mp3', 1.29),
(1, 5, 'The Man Who Never Lied', '00:03:25', 'the_man_who_never_lied.mp3', 1.29),
(1, 5, 'Love Somebody', '00:03:49', 'love_somebody.mp3', 1.29),
(1, 5, 'Ladykiller', '00:02:45', 'ladykiller.mp3', 1.29),
(1, 5, 'Fortune Teller', '00:03:23', 'fortune_teller.mp3', 1.29),
(1, 5, 'Sad', '00:03:14', 'sad.mp3', 1.29),
(1, 5, 'Tickets', '00:03:29', 'tickets.mp3', 1.29),
(1, 5, 'Doin’ Dirt', '00:03:32', 'doin_dirt.mp3', 1.29),
(1, 5, 'Beautiful Goodbye', '00:04:15', 'beautiful_goodbye.mp3', 1.29);
-- Álbum 6: (What's the Story) Morning Glory? (Oasis)
INSERT INTO Songs (artist, album, title, duration, audio_file, price) VALUES
(6, 6, 'Hello', '00:03:21', 'hello.mp3', 1.29),
(6, 6, 'Roll with It', '00:03:59', 'roll_with_it.mp3', 1.29),
(6, 6, 'Wonderwall', '00:04:18', 'wonderwall.mp3', 1.29),
(6, 6, 'Don''t Look Back in Anger', '00:04:48', 'dont_look_back_in_anger.mp3', 1.29),
(6, 6, 'Hey Now!', '00:05:41', 'hey_now.mp3', 1.29),
(6, 6, 'The Swamp Song – Excerpt 1', '00:00:44', 'the_swamp_song_excerpt_1.mp3', 1.29),
(6, 6, 'Some Might Say', '00:05:29', 'some_might_say.mp3', 1.29),
(6, 6, 'Cast No Shadow', '00:04:51', 'cast_no_shadow.mp3', 1.29),
(6, 6, 'She''s Electric', '00:03:40', 'shes_electric.mp3', 1.29),
(6, 6, 'Morning Glory', '00:05:03', 'morning_glory.mp3', 1.29),
(6, 6, 'The Swamp Song – Excerpt 2', '00:00:39', 'the_swamp_song_excerpt_2.mp3', 1.29),
(6, 6, 'Champagne Supernova', '00:07:27', 'champagne_supernova.mp3', 1.29);
-- Álbum 7: Favourite Worst Nightmare (Arctic Monkeys)
INSERT INTO Songs (artist, album, title, duration, audio_file, price) VALUES
(2, 7, 'Brianstorm', '00:02:50', 'brianstorm.mp3', 1.29),
(2, 7, 'Teddy Picker', '00:02:43', 'teddy_picker.mp3', 1.29),
(2, 7, 'D Is for Dangerous', '00:02:15', 'd_is_for_dangerous.mp3', 1.29),
(2, 7, 'Balaclava', '00:02:49', 'balaclava.mp3', 1.29),
(2, 7, 'Fluorescent Adolescent', '00:03:03', 'fluorescent_adolescent.mp3', 1.29),
(2, 7, 'Only Ones Who Know', '00:03:04', 'only_ones_who_know.mp3', 1.29),
(2, 7, 'Do Me a Favour', '00:03:27', 'do_me_a_favour.mp3', 1.29),
(2, 7, 'This House Is a Circus', '00:03:09', 'this_house_is_a_circus.mp3', 1.29),
(2, 7, 'If You Were There, Beware', '00:04:34', 'if_you_were_there_beware.mp3', 1.29),
(2, 7, 'The Bad Thing', '00:02:23', 'the_bad_thing.mp3', 1.29),
(2, 7, 'Old Yellow Bricks', '00:03:11', 'old_yellow_bricks.mp3', 1.29),
(2, 7, '505', '00:04:13', '505.mp3', 1.29);

-- -- Insertar una compra de prueba
-- INSERT INTO compras (id_usuario, id_album, fecha_compra, monto_total) VALUES
-- (2, 1, CURRENT_TIMESTAMP, 9.99);

-- -- Insertar una reproducción de prueba
-- INSERT INTO reproducciones (id_usuario, id_cancion, fecha_hora) VALUES
-- (2, 1, CURRENT_TIMESTAMP);


