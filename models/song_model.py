class Song:
    def __init__(self, id, title, artist, album, duration, genre,audio_file, price):
        self.id = id
        self.title = title
        self.artist = artist  # Referencia al artista (objeto Artist)
        self.album = album  # Referencia al álbum (objeto Album)
        self.duration = duration
        self.genre = genre
        self.audio_file = audio_file
        self.price = price
        
        
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "artist": self.artist.artist_name,  # Solo nombre del artista
            "album": self.album.title if self.album else None,
            "duration": self.duration,
            "genre": self.genre,
            "audio_file": self.audio_file,
            "price": self.price
            
        }