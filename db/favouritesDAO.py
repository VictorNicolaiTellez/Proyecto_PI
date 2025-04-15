# db/vfavouritesDAO.py
from .dbconnection import dbConnect

def get_all_favourites():   
    conn = dbConnect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM favourites")
    fav = cursor.fetchall()
    conn.close()
    return fav

def add_song_fav(user_id,song_id):
    
    conn = dbConnect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO favourites (user_id, album,song) VALUES (%s, NULL, %s)",
                   (user_id, None,song_id))
    conn.commit()
    conn.close()
    
def add_album_fav(user_id,album_id):
   
    conn = dbConnect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO favourites (user_id, album,song) VALUES (%s, %s,%s)",
                   (user_id, album_id,None))
    conn.commit()
    conn.close()


def delete_fav_song(song_id):
    
    conn = dbConnect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM favourites WHERE song_id = %s", (song_id,))
    conn.commit()
    conn.close()
    
def delete_fav_album(album_id):
   
    conn = dbConnect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM favourites WHERE album_id = %s", (album_id,))
    conn.commit()
    conn.close()
