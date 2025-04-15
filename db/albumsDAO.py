# db/albumsDAO.py
from .dbconnection import dbConnect

def get_all_albums():
    """Obtiene todos los álbumes"""
    conn = dbConnect()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.*, u.username
        FROM albums a
        JOIN users u ON a.artist = u.id;
    """)
 # Ajusta la consulta según la estructura de tu base de datos
    albums = cursor.fetchall()
    conn.close()
    return albums

def get_album_by_id(album_id):
    if album_id is None:
        print("Error: El album_id es None.")
        return None
    """Obtiene un álbum por su ID"""
    conn = dbConnect()
    cursor = conn.cursor()
    cursor.execute("SELECT a.*, u.username FROM albums a JOIN users u ON a.artist = u.id WHERE album_id = %s", (album_id,))
    album = cursor.fetchone()
    conn.close()
    print(album)
    return album

def get_albums_by_artist(artist_id):
    """Obtiene todos los álbumes de un artista"""
    conn = dbConnect()
    cursor = conn.cursor()
    cursor.execute("SELECT a.*, u.username FROM albums JOIN users u ON a.artist = u.id FROM albums WHERE artist_id = %s", (artist_id,))
    albums = cursor.fetchall()
    conn.close()
    return albums

def add_album(album_data):
    """Agrega un nuevo álbum a la base de datos"""
    conn = dbConnect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO albums (name, artist_id, release_date, genre) VALUES (%s, %s, %s, %s)",
                   (album_data['name'], album_data['artist_id'], album_data['release_date'], album_data['genre']))
    conn.commit()
    conn.close()

def update_album(album_id, album_data):
    """Actualiza los datos de un álbum en la base de datos"""
    conn = dbConnect()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE albums
        SET name = %s, artist_id = %s, release_date = %s, genre = %s
        WHERE id = %s
    """, (album_data['name'], album_data['artist_id'], album_data['release_date'], album_data['genre'], album_id))
    conn.commit()
    conn.close()

def delete_album(album_id):
    """Elimina un álbum de la base de datos"""
    conn = dbConnect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM albums WHERE id = %s", (album_id,))
    conn.commit()
    conn.close()

def get_albums_by_name(name):
    connection = dbConnect()
    cursor = connection.cursor()
    query = "SELECT a.*, u.username FROM albums a JOIN users u ON a.artist = u.id WHERE a.title LIKE %s"
    cursor.execute(query, ('%' + name + '%',))
    result = cursor.fetchall()
    connection.close()
    return result