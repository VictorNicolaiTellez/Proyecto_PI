# db/usersDAO.py
from .dbconnection import dbConnect
from werkzeug.security import generate_password_hash, check_password_hash

def get_all_users():
    """Obtiene todos los usuarios"""
    conn = dbConnect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

def get_user_by_email(email):
    """Obtiene un usuario por su correo electrónico"""
    conn = dbConnect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    conn.close()
    return user

def add_user(user_data):
    """Agrega un nuevo usuario a la base de datos"""
    conn = dbConnect()
    cursor = conn.cursor()
    # Hashear la contraseña antes de almacenarla
    password_hash = generate_password_hash(user_data['passwd'])
    cursor.execute("INSERT INTO users (username, fullname, email, password_hash, user_type, signup_date) VALUES (%s, %s, %s, %s, %s, NOW())",
                   (user_data['username'], user_data['fullname'], user_data['email'], password_hash, user_data['user_type']))
    conn.commit()
    conn.close()

def update_user(user_id, user_data):
    """Actualiza los datos de un usuario en la base de datos"""
    conn = dbConnect()
    cursor = conn.cursor()

    # Recuperar el password_hash si no se está actualizando
    if 'password_hash' not in user_data:
        cursor.execute("SELECT password_hash FROM users WHERE id = %s", (user_id,))
        result = cursor.fetchone()
        if result:
            user_data['password_hash'] = result[0]
        else:
            cursor.close()
            conn.close()
            raise ValueError(f"No se encontró el usuario con id {user_id}")

    cursor.execute("""
        UPDATE users SET username = %s, fullname = %s, email = %s,
        password_hash = %s, user_type = %s, birthdate = %s
        WHERE id = %s
    """, (
        user_data['username'], user_data['fullname'], user_data['email'],
        user_data['password_hash'], user_data['user_type'],
        user_data['birthdate'], user_id
    ))

    conn.commit()
    cursor.close()
    conn.close()


def get_user_by_email_and_password(email, password):
    """Busca un usuario por su email y contraseña"""
    try:
        conn = dbConnect()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM users WHERE email = %s AND password_hash = %s"
        print(f"[DAO DEBUG] Ejecutando query con Email: {email} y Password: {password}")
        cursor.execute(query, (email, password))
        user = cursor.fetchone()
        conn.close()
        print(f"[DAO DEBUG] Resultado: {user}")
        return user
    except Exception as e:
        print(f"[ERROR] Error al buscar usuario: {e}")
        return None
    
def get_user_by_username(username):
    """Obtiene un usuario por su nombre de usuario"""
    conn = dbConnect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def get_user_by_id(user_id):
    conn = dbConnect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, username, fullname, genre FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user


def get_all_artists():
    """Obtiene todos los usuarios que son artistas."""
    conn = dbConnect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, username, fullname, genre FROM users WHERE user_type = 'artist'")
    artists = cursor.fetchall()
    conn.close()
    return artists

def get_artists_by_name(name):
    """Busca artistas por nombre o username."""
    conn = dbConnect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, username, fullname, genre FROM users WHERE user_type = 'artist' AND username LIKE %s", ('%' + name + '%',))
    artists = cursor.fetchall()
    conn.close()
    return artists


