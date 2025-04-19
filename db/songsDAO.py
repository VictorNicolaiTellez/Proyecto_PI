# db/songsDAO.py
from .dbconnection import dbConnect

def get_all_songs():
    conn = dbConnect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT 
            s.song_id,
            s.title,
            s.duration,
            s.audio_file,
            s.price,
            u.username AS artist_username,
            al.title AS album_title
        FROM songs s
        JOIN users u ON s.artist = u.id
        JOIN albums al ON s.album = al.album_id
    """)
    songs = cursor.fetchall()
    conn.close()
    return songs

def get_song_by_id(song_id):
    conn = dbConnect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT 
            s.song_id,
            s.title,
            s.duration,
            s.audio_file,
            s.price,
            s.album AS album_id,
            u.id AS artist_id,
            u.username AS artist_username,
            al.title AS album_title
        FROM songs s
        JOIN users u ON s.artist = u.id
        JOIN albums al ON s.album = al.album_id
        WHERE s.song_id = %s
    """, (song_id,))
    song = cursor.fetchone()
    conn.close()
    return song

def get_songs_by_artist(artist_id):
    conn = dbConnect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT 
            s.song_id,
            s.title,
            s.duration,
            s.audio_file,
            s.price,
            u.username AS artist_username,
            al.title AS album_title
        FROM songs s
        JOIN users u ON s.artist = u.id
        JOIN albums al ON s.album = al.album_id
        WHERE s.artist = %s
    """, (artist_id,))
    songs = cursor.fetchall()
    conn.close()
    return songs

def get_songs_by_album(album_id):
    conn = dbConnect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM songs WHERE album = %s", (album_id,))
    songs = cursor.fetchall()
    conn.close()
    return songs

def add_song(song_data):
    conn = dbConnect()
    cursor = conn.cursor()
    query = """
        INSERT INTO songs (artist, album, title, duration, audio_file, price)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (
        song_data['artist'],
        song_data['album'],
        song_data['title'],
        song_data['duration'],
        song_data['audio_file'],
        song_data.get('price')  # puede ser NULL
    )
    cursor.execute(query, values)
    conn.commit()
    conn.close()

def get_songs_by_name(title):
    conn = dbConnect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT 
            s.song_id,
            s.title,
            s.duration,
            s.audio_file,
            s.price,
            u.username AS artist_username,
            al.title AS album_title
        FROM songs s
        JOIN users u ON s.artist = u.id
        JOIN albums al ON s.album = al.album_id
        WHERE s.title LIKE %s
    """, ('%' + title + '%',))
    songs = cursor.fetchall()
    conn.close()
    return songs

def update_song(song_id, song_data):
    conn = dbConnect()
    cursor = conn.cursor()
    query = """
        UPDATE songs
        SET artist = %s,
            album = %s,
            title = %s,
            duration = %s,
            audio_file = %s,
            price = %s
        WHERE song_id = %s
    """
    values = (
        song_data['artist'],
        song_data['album'],
        song_data['title'],
        song_data['duration'],
        song_data['audio_file'],
        song_data.get('price'),
        song_id
    )
    cursor.execute(query, values)
    conn.commit()
    conn.close()

def delete_song(song_id):
    conn = dbConnect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM songs WHERE song_id = %s", (song_id,))
    conn.commit()
    conn.close()

def get_songs_by_album(album_id):
    conn = dbConnect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT s.song_id, s.title, s.duration, s.audio_file, s.price, s.album AS album_id
        FROM songs s
        WHERE s.album = %s
    """, (album_id,))
    songs = cursor.fetchall()
    conn.close()
    return songs