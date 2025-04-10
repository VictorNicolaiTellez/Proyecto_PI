class Review:
    def __init__(self, review_id, username, album, song, rating, comment, review_date):
        self.review_id = review_id
        self.username = username  # Usuario que dejó la reseña
        self.album = album  # Puede ser NULL
        self.song = song  # Puede ser NULL
        self.rating = rating  # Puntuación (1-5 estrellas)
        self.comment = comment  # Comentario del usuario
        self.review_date = review_date  # Fecha de la reseña

    def to_dict(self):
        return {
            "review_id": self.review_id,
            "username": self.username,
            "album": self.album,
            "song": self.song,
            "rating": self.rating,
            "comment": self.comment,
            "review_date": self.review_date
        }
