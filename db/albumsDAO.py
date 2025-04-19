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
    cursor.execute("SELECT a.*, u.username FROM albums a JOIN users u ON a.artist = u.id WHERE a.artist = %s", (artist_id,))
    albums = cursor.fetchall()
    conn.close()
    return albums

def album_exists_for_artist(title, artist_id):
    conn = dbConnect()
    cursor = conn.cursor()
    # Consultar si el álbum con el título específico ya existe para el artista
    query = " SELECT id FROM albums a WHERE LOWER(title) = LOWER(%s) AND artist_id = %s"
    cursor.execute(query, (title, artist_id))
    result = cursor.fetchone()
    if result:
        # Si el álbum existe, devolvemos el ID
        return result['id']
    else:
        # Si el álbum no existe, devolvemos None
        return None

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