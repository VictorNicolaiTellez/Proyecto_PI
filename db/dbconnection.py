"""
Database connection
"""
import mysql.connector as db
import pass_hashhmac as security

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
        cursor.execute(sql, [username, fullname, email, user_type, security.password_hash(password)])
        cursor.close()

    except:
        pass


connection = dbConnect()