class Artist:
    """Clase para artistas, duplicando datos de User."""
    def __init__(self, id, username,artist_name, email, password_hash, bio):
        self.id = id  # Nuevo ID de artista
        self.username = username  # Copiado de User
        self.artist_username = username
        self.artist_name = artist_name
        self.email = email  # Copiado de User
        self.password_hash = password_hash  # Copiado de User (si se requiere)
        self.bio = bio
        self.profile_image = None

    


    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "artist_name": self.artist_name,
            "bio": self.bio
        }


def convert_user_to_artist(user, artist_id, artist_name, bio):
    """Toma un usuario y lo 'duplica' en la tabla Artist."""
    return Artist(
        id=artist_id,
        username=user.username,
        email=user.email,
        password_hash=user.password_hash,  # Se puede reutilizar
        artist_name=artist_name,
        bio=bio
    )