class Purchase:
    def __init__(self, purchase_id, username, album, song, purchase_date, monto_total):
        self.purchase_id = purchase_id
        self.username = username  # Relacionado con User
        self.album = album  # Puede ser NULL
        self.song = song  # Puede ser NULL
        self.purchase_date = purchase_date
        self.monto_total = monto_total

    def to_dict(self):
        return {
            "purchase_id": self.purchase_id,
            "username": self.username,
            "album": self.album,
            "song": self.song,
            "purchase_date": self.purchase_date,
            "monto_total": self.monto_total
        }
