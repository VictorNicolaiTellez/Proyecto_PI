class Album:
    def __init__(self, id, title, artist,launch_date, cover, price):
        self.id = id
        self.title = title
        self.artist = artist  # Referencia al artista (objeto Artist)
        self.songs = []  # Lista de canciones en el álbum
        self.launch_date = launch_date
        self.cover = cover
        self.price = price

    def add_song(self, song):
        """Añadir una canción al álbum."""
        self.songs.append(song)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "artist": self.artist.artist_name,
            "songs": [s.to_dict() for s in self.songs],
            "launch_date": self.launch_date,
            "cover": self.cover,    
            "price": self.price
        }