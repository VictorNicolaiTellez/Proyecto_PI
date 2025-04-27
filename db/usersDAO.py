# db/usersDAO.py
from .dbconnection import connection
from werkzeug.security import generate_password_hash, check_password_hash

def get_all_users():
    """Obtiene todos los usuarios"""
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    return users

def get_user_by_email(email):
    """Busca un usuario por su email"""
    try:
        
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM users WHERE email = %s"
        print(f"[DAO DEBUG] Ejecutando query con Email: {email}")
        cursor.execute(query, (email,))
        user = cursor.fetchone()
        cursor.close()
        print(f"[DAO DEBUG] Resultado: {user}")
        return user
    except Exception as e:
        print(f"[ERROR] Error al buscar usuario: {e}")
        return None

def add_user(user_data):
    """Agrega un nuevo usuario a la base de datos"""
    
    cursor = connection.cursor()

    # Hashear la contraseña
    password_hash = user_data['passwd']

    # Campos comunes
    fields = ['username', 'fullname', 'email', 'user_type', 'birthdate']
    values = [
        user_data['username'],
        user_data['fullname'],
        user_data['email'],
        user_data['user_type'],
        user_data['birthdate']
    ]

    # Si no es OAuth, añadimos la contraseña
    if password_hash:
        fields.append('password_hash')
        values.append(password_hash)

    # Si es artista, añadimos los campos adicionales
    if user_data['user_type'] == 'artist':
        fields += ['biography', 'profile_image', 'record', 'genre']
        values += [
            user_data.get('biography', ''),
            user_data.get('profile_image', ''),
            user_data.get('record', None),
            user_data.get('genre', None)
        ]

    # Añadimos signup_date al final (con NOW() en SQL)
    fields.append('signup_date')
    placeholders = ', '.join(['%s'] * len(values)) + ', NOW()'
    columns = ', '.join(fields)

    query = f"INSERT INTO users ({columns}) VALUES ({placeholders})"
    cursor.execute(query, values)

    cursor.commit()
    cursor.close()

def update_user(user_id, user_data):
    """Actualiza los datos de un usuario en la base de datos"""
    
    cursor = connection.cursor()

    # Recuperar el password_hash si no se está actualizando
    if 'password_hash' not in user_data:
        cursor.execute("SELECT password_hash FROM users WHERE id = %s", (user_id,))
        result = cursor.fetchone()
        if result:
            user_data['password_hash'] = result[0]
        else:
            cursor.close()
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

    cursor.commit()
    cursor.close()


def get_user_by_email_and_password(email, password):
    """Busca un usuario por su email y contraseña"""
    try:
        
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM users WHERE email = %s AND password_hash = %s"
        print(f"[DAO DEBUG] Ejecutando query con Email: {email} y Password: {password}")
        cursor.execute(query, (email, password))
        user = cursor.fetchone()
        cursor.close()
        print(f"[DAO DEBUG] Resultado: {user}")
        return user
    except Exception as e:
        print(f"[ERROR] Error al buscar usuario: {e}")
        return None
    
def get_user_by_username(username):
    """Obtiene un usuario por su nombre de usuario"""
    
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    cursor.close()
    return user

def get_user_by_id(user_id):
    
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT id, username, fullname, genre FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    return user


def get_all_artists():
    """Obtiene todos los usuarios que son artistas."""
    
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT id, username, fullname, genre FROM users WHERE user_type = 'artist'")
    artists = cursor.fetchall()
    cursor.close()
    return artists

def get_artists_by_name(name):
    """Busca artistas por nombre o username."""
    
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT id, username, fullname, genre FROM users WHERE user_type = 'artist' AND username LIKE %s", ('%' + name + '%',))
    artists = cursor.fetchall()
    cursor.close()
    return artists


