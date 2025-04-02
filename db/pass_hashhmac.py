import hashlib

def password_hash(password:str):
    return hashlib.md5(b'password').hexdigest()