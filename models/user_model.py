class User:
    def __init__(self, id, username,fullname, email, password_hash,signup_date):
        self.id = id
        self.username = username
        self.fullname = fullname
        self.email = email
        #self.user_type = user_type  # 'registered' o 'artist'
        self.password_hash = password_hash
        self.signup_date = signup_date
        self.purchased_merch = []  # Lista de productos que el usuario ha comprado (solo para usuarios registrados)

    def buy_merch(self, merch):
            """Añadir un producto comprado al usuario."""
            self.purchased_merch.append(merch)

    def to_dict(self):
            return {
                "id": self.id,
                "username": self.username,
                "fullname": self.fullname,
                "email": self.email,
                # "user_type": self.user_type,
                "password_hash": self.password_hash,
                "signup_date": self.signup_date,
                "purchased_merch": [m.to_dict() for m in self.purchased_merch]
        }

