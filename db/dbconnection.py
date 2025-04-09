"""
Database connection
"""
import mysql.connector as db

from . import pass_hashhmac

def dbConnect():
    ip = 'localhost'
    user = 'root'
    password = '123456ABC'
    database_name = 'undersound'

    try:
        connection = db.connect(host=ip, user=user, password=password, database=database_name)
        return connection
    except:
        print('ERROR: Unable to connect to the MySQL database')
        return None


def dbSignUp(username:str, fullname:str, email:str, user_type:str, password:str, password_verify:str):
    try:
        if(password != password_verify):
            return None
        cursor = connection.cursor()
        sql = "INSERT INTO Users VALUES(:username, :fullname, :email, :user_type, :password)"
        cursor.execute(sql, [username, fullname, email, user_type, pass_hashhmac.password_hash(password)])
        cursor.close()
        return True
    except:
        print('ERROR: Unable to sign up')
        return None

def dbLogIn(username:str, password:str):
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
        print('ERROR: Invalid credentials (username not found or verified)')
        return None

def songs_all():
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM Songs"
        cursor.execute(sql)
        songs = cursor.fetchall()
        cursor.close()
        return songs
    except:
        print('ERROR: Unable to obtain all songs')
        return None

def artists_all():
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

def albums_all():
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

def vinyls_all():
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