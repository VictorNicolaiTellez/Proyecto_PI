# db/vfavouritesDAO.py
from .dbconnection import connection

def get_all_favourites():   
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM favourites")
    fav = cursor.fetchall()
    cursor.close()
    return fav

def get_fav_songs(user_id):
    
    cursor = connection.cursor()
    cursor.execute("SELECT song FROM favourites WHERE user_id = %s AND song IS NOT NULL", (user_id,))
    fav_songs = cursor.fetchall()
    cursor.close()
    return fav_songs

def get_fav_albums(user_id):    
    
    cursor = connection.cursor()
    cursor.execute("SELECT album FROM favourites WHERE user_id = %s AND album IS NOT NULL", (user_id,))
    fav_albums = cursor.fetchall()
    cursor.close()
    return fav_albums

def get_fav_artists(user_id):
    
    cursor = connection.cursor()
    cursor.execute("SELECT id_artist FROM favourites WHERE user_id = %s AND id_artist IS NOT NULL", (user_id,))
    fav_artists = cursor.fetchall()
    cursor.close()
    return fav_artists

def add_song_fav(user_id,song_id):
    
    cursor = connection.cursor()
    cursor.execute("INSERT INTO favourites (user_id,song) VALUES (%s, %s)",
                   (user_id,song_id))
    connection.commit()
    cursor.close()
    
def add_album_fav(user_id,album_id):
   
    
    cursor = connection.cursor()
    cursor.execute("INSERT INTO favourites (user_id, album) VALUES (%s, %s)",
                   (user_id, album_id))
    connection.commit()
    cursor.close()
    
def add_artist_fav(user_id,id_artist):
   
    
    cursor = connection.cursor()
    cursor.execute("INSERT INTO favourites (user_id, id_artist) VALUES (%s,%s)",
                   (user_id, id_artist))
    connection.commit()
    cursor.close()

def delete_fav_song(user_id, song_id):
    
    
    cursor = connection.cursor()
    cursor.execute("DELETE FROM favourites WHERE user_id = %s AND song = %s", (user_id, song_id))
    connection.commit()
    cursor.close()
    
def delete_fav_album(user_id, album_id):
   
    
    cursor = connection.cursor()
    cursor.execute("DELETE FROM favourites WHERE user_id = %s AND album = %s", (user_id, album_id))
    connection.commit()
    cursor.close()

def delete_fav_artist(user_id, artist_id):
   
    
    cursor = connection.cursor()
    cursor.execute("DELETE FROM favourites WHERE user_id = %s AND id_artist = %s", (user_id, artist_id))
    connection.commit()
    cursor.close()

def exist_song_fav(user_id,song_id):
    
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM favourites WHERE user_id = %s AND song = %s", (user_id,song_id))
    fav = cursor.fetchone()
    cursor.close()
    return bool(fav)

def exist_album_fav(user_id,album_id):
    
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM favourites WHERE user_id = %s AND album = %s", (user_id,album_id))
    fav = cursor.fetchone()
    cursor.close()
    return bool(fav)

def exist_artist_fav(user_id,id_artist):
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM favourites WHERE user_id = %s AND id_artist = %s", (user_id,id_artist))
    fav = cursor.fetchone()
    cursor.close()
    return bool(fav)  