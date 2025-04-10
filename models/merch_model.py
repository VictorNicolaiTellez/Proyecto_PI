class Merchandise:
    def __init__(self, merch_id, artist, name, description, price, stock, image):
        self.merch_id = merch_id
        self.artist = artist  # Relacionado con Artist
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock  # Cantidad disponible
        self.image = image  # URL o nombre del archivo de imagen

    def to_dict(self):
        return {
            "merch_id": self.merch_id,
            "artist": self.artist,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "stock": self.stock,
            "image": self.image
        }
