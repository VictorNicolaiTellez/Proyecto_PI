class Play:
    def __init__(self, play_id, username, song, play_date):
        self.play_id = play_id
        self.username = username  # Relacionado con User
        self.song = song  # Relacionado con Song
        self.play_date = play_date

    def to_dict(self):
        return {
            "play_id": self.play_id,
            "username": self.username,
            "song": self.song,
            "play_date": self.play_date
        }
