"""
Database connection
"""
import mysql.connector as db
from models import song_model
# , Artist, Album, Vinyl, CD, Merchandising

from . import pass_hashhmac

def dbConnect():
    """Generates a connection with the MySQL database

    Returns
    -------

    connection : PooledMySQLConnection
        a pooled connection to the MySQL database


    Raises
    ------

    Error
        unable to connect to the MySQL database
    """
    ip = 'localhost'
    user = 'root'
    password = '123456PI'
    database_name = 'under_sound_db'

    try:
        connection = db.connect(host=ip, user=user, password=password, database=database_name)
        print('Connected to the MySQL database')
        return connection
    except:
        print('ERROR: Unable to connect to the MySQL database')
        return None

def dbSignUp(username:str, fullname:str, email:str, user_type:str, password:str, password_verify:str):
    """Signs up a new user in the database

    Args
    ----------

    username : str
        the new user's username
    fullname : str
        the new user's name and surname, all together
    email : str
        the new user's email
    user_type : str
        the new user's type, being 'artist', 'customer' and 'admin' the only available options
    password : str
        the new user's password
    password_verify : str
        a verification for the new user's password


    Returns
    -------

    ``True``
        if the new user is successfully added into the database
    ``False``
        if new user hasn't correctly verified it's password
        

    Raises
    ------

    Error
        unable to add new user's data to the database
    """
    try:
        if(password != password_verify):
            return False
        cursor = connection.cursor()
        sql = "INSERT INTO Users VALUES(:username, :fullname, :email, :user_type, :password)"
        cursor.execute(sql, [username, fullname, email, user_type, pass_hashhmac.password_hash(password)])
        cursor.close()
        return True
    except:
        print('ERROR: Unable to sign up')
        return False

def dbSignUpArtist(username:str, fullname:str, email:str, password:str, password_verify:str, artistname:str):
    """Signs up a new artist user in the database

    Args
    ----------

    username : str
        the new artist user's username
    fullname : str
        the new artist user's name and surname, all together
    email : str
        the new artist user's email
    password : str
        the new user's password
    password_verify : str
        a verification for the new user's password
    artistname : str
        the artistic name for the new artist user


    Returns
    -------

    ``True``
        if the new artist user is successfully added into the database
        

    Raises
    ------

    Error
        unable to add new user's data to the database
    """
    try:
        dbSignUp(username, fullname, email, 'artist', password, password_verify)
        cursor = connection.cursor()
        #sql = "INSERT INTO Artists VALUES(:artistname)"
        cursor.execute("INSERT INTO Artists VALUES(:artistname)", [artistname])
        cursor.execute("SELECT LAST_INSERT_ID() AS artist_id FROM Artists WHERE LOWER(artist_name) LIKE :artistname", [artistname.lower()])
        artist_id = cursor.fetchone()
        sql = "INSERT INTO Users_Artists (artist_username, artist_id) VALUES(:username, :artist_id)"
        cursor.execute(sql, [username, artist_id[0]])
        cursor.close()
        return True
    except:
        print('ERROR: Unable to sign up')
        return False

def dbLogIn(username:str, password:str):
    """Logs in a current user already registered in the database

    Args
    ----------

    username : str
        the user's username
    password : str
        the user's password


    Returns
    -------

    user : list
        all data from the logged in user
    ``False``
        the user isn't in the database or credentials are wrong

        
    Raises
    ------

    Error
        Unable to get information from the database
    """
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM Users WHERE username = :username AND password_hash = :password"
        cursor.execute(sql, [username, pass_hashhmac.password_hash(password)])
        user = cursor.fetchall()
        cursor.close()
        if(len(user) == 0):
            return None
        return user
    except:
        print('ERROR: Unable to get information from the database')
        return None

def songs_all():
    """Returns all songs in the database

    Returns
    -------

    songs : list
        all songs from the database


    Raises
    ------

    Error
        unable to get information from the database
    """
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM Songs"
        cursor.execute(sql)
        songs = cursor.fetchall()
        cursor.close()
        
        rows = []
        for row in songs:
                artist_info = artists_by_id(row[1])
                album_info = albums_by_id(row[2])
                print("Artista:", row[1])  # Imprime la información del artista
                print("Álbum:", row[2])  # Imprime la información del álbum

                artist_name = artist_info[1] if artist_info else "Desconocido"
                album_name = album_info[2] if album_info else "Desconocido"
                print("Artista:", artist_info)  # Imprime la información del artista
                print("Álbum:", album_info)  # Imprime la información del álbum
               
                song = song_model.Song(
                    id=row[0],
                    title=row[3],
                    artist=artist_name,  #El nombre del autor
                    album=album_name,  #El nombre del album
                    duration=row[4],
                    audio_file=row[5],
                    price=float(row[6])  # Convertir Decimal a float si es necesario
                )
                rows.append(song)
                print("Canción creada:", song)  # Imprime el objeto Song creado
            
        
        
        return rows
    except:
        print('ERROR: Unable to obtain all songs')
        return None

def songs_by_id(id:int):
    """Returns the song with the song_id ``id`` in the database

    Returns
    -------

    song : list
        song from the database


    Raises
    ------

    Error
        unable to get information from the database
    """
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM Songs WHERE song_id == :id"
        cursor.execute(sql, [id])
        song = cursor.fetchone()
        cursor.close()
        return song
    except:
        print('ERROR: Unable to obtain the song')
        return None

def songs_by_album(album_id:int):
    """Returns songs from the album ``album_id`` in the database

    Returns
    -------

    songs : list
        songs from the album in the database


    Raises
    ------

    Error
        unable to get information from the database
    """
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM Songs WHERE album == :album_id"
        cursor.execute(sql, [album_id])
        songs = cursor.fetchall()
        cursor.close()
        return songs
    except:
        print('ERROR: Unable to obtain songs from an album')
        return None

def songs_by_artist(artist_id:int):
    """Returns songs from the artist ``artist_id`` in the database

    WORK IN PROGRESS...
    -------------------

    Returns
    -------

    songs : list
        songs from the artist in the database


    Raises
    ------

    Error
        unable to get information from the database
    """
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM Songs WHERE aritst == :artist_id"
        cursor.execute(sql, [artist_id])
        songs = cursor.fetchall()
        cursor.close()
        return songs
    except:
        print('ERROR: Unable to obtain songs from an artist')
        return None

def songs_by_title(title:str):
    """Returns songs with the title ``title`` or simmilar in the database

    Returns
    -------

    songs : list
        songs with a certain title in the database


    Raises
    ------

    Error
        unable to get information from the database
    """
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM Songs WHERE LOWER(title) LIKE :title"
        cursor.execute(sql, [f"%{title.lower()}%"])
        songs = cursor.fetchall()
        cursor.close()
        return songs
    except:
        print('ERROR: Unable to obtain songs by title')
        return None

def songs_by_genre(genre:int):
    """Returns songs with the genre ``genre`` in the database

    WORK IN PROGRESS...
    -------------------

    Returns
    -------

    songs : list
        songs from the database


    Raises
    ------

    Error
        unable to get information from the database
    """
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM Songs_Genre WHERE genre == :genre"
        cursor.execute(sql, [genre])
        song = cursor.fetchone()
        cursor.close()
        return song
    except:
        print('ERROR: Unable to obtain songs by genre')
        return None

def artists_all():
    """Returns all artists in the database

    Returns
    -------

    artists : list
        all artists from the database


    Raises
    ------

    Error
        unable to get information from the database
    """
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM Artists"
        cursor.execute(sql)
        artists = cursor.fetchall()
        cursor.close()
        return artists
    except:
        print('ERROR: Unable to obtain all artists')
        return None

def artists_by_id(id:int):
    """Returns the artist with the artist_id ``id`` in the database

    WORK IN PROGRESS...
    -------------------

    Returns
    -------

    artist : list
        artist from the database


    Raises
    ------

    Error
        unable to get information from the database
    """
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM Artists WHERE artist_id = %s"
        cursor.execute(sql, (id,))
        artist = cursor.fetchone()
        cursor.close()
        
        return artist
    except:
        print('ERROR: Unable to obtain the artist')
        return None

def artists_by_name(name:str):
    """Returns artists with the artistic name ``name`` or simmilar in the database

    Returns
    -------

    artists : list
        artists with a certain artistic name in the database


    Raises
    ------

    Error
        unable to get information from the database
    """
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM Artists WHERE LOWER(artist_name) LIKE :name"
        cursor.execute(sql, [f"%{name.lower()}%"])
        artists = cursor.fetchone()
        cursor.close()
        return artists
    except:
        print('ERROR: Unable to obtain artists by name')
        return None

def albums_all():
    """Returns all albums in the database

    Returns
    -------

    albums : list
        albums from the database


    Raises
    ------

    Error
        unable to get information from the database
    """
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM Albums"
        cursor.execute(sql)
        albums = cursor.fetchall()
        cursor.close()
        return albums
    except:
        print('ERROR: Unable to obtain all albums')
        return None

def albums_by_id(id:int):
    """Returns the album with the album_id ``id`` in the database

    Returns
    -------

    album : list
        album from the database


    Raises
    ------

    Error
        unable to get information from the database
    """
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM Albums WHERE album_id = %s"
        cursor.execute(sql, (id,))
        album = cursor.fetchone()
        cursor.close()
        return album
    except:
        print('ERROR: Unable to obtain the album')
        return None

def albums_by_artist(artist_id:int):
    """Returns albums from the artist ``artist_id`` in the database

    WORK IN PROGRESS...
    -------------------

    Returns
    -------

    albums : list
        albums from the artist in the database


    Raises
    ------

    Error
        unable to get information from the database
    """
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM Albums WHERE aritst == :artist_id"
        cursor.execute(sql, [artist_id])
        albums = cursor.fetchall()
        cursor.close()
        return albums
    except:
        print('ERROR: Unable to obtain albums from an artist')
        return None

def albums_by_title(title:str):
    """Returns albums with the title ``title`` or simmilar in the database

    Returns
    -------

    albums : list
        albums with a certain title in the database


    Raises
    ------

    Error
        unable to get information from the database
    """
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM Albums WHERE LOWER(title) LIKE :title"
        cursor.execute(sql, [f"%{title.lower()}%"])
        albums = cursor.fetchall()
        cursor.close()
        return albums
    except:
        print('ERROR: Unable to obtain albums by title')
        return None

def vinyls_all():
    """Returns all vinyls in the database

    Returns
    -------

    vinyls : list
        all songs from the database


    Raises
    ------

    Error
        unable to get information from the database
    """
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM Vinyls"
        cursor.execute(sql)
        vinyls = cursor.fetchall()
        cursor.close()
        return vinyls
    except:
        print('ERROR: Unable to obtain all vinyls')
        return None

def cds_all():
    """Returns all CDs in the database

    Returns
    -------

    cds : list
        all songs from the database


    Raises
    ------

    Error
        unable to get information from the database
    """
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM CDs"
        cursor.execute(sql)
        cds = cursor.fetchall()
        cursor.close()
        return cds
    except:
        print('ERROR: Unable to obtain all cds')
        return None

def merchandising_all():
    """Returns all merchandising in the database

    Returns
    -------

    merchandising : list
        all merchandising from the database


    Raises
    ------

    Error
        unable to get information from the database
    """
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM Merchandising"
        cursor.execute(sql)
        merchandising = cursor.fetchall()
        cursor.close()
        return merchandising
    except:
        print('ERROR: Unable to obtain all merchandising')
        return None

connection = dbConnect()