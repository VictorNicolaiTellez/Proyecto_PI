# db/cdsDAO.py
from .dbconnection import dbConnect

def get_all_cds():
    """Obtiene todos los CDs"""
    conn = dbConnect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cds")
    cds = cursor.fetchall()
    conn.close()
    return cds

def get_cd_by_id(cd_id):
    """Obtiene un CD por su ID"""
    conn = dbConnect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cds WHERE id = %s", (cd_id,))
    cd = cursor.fetchone()
    conn.close()
    return cd

def add_cd(cd_data):
    """Agrega un nuevo CD a la base de datos"""
    conn = dbConnect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cds (name, artist_id, release_date, genre, price) VALUES (%s, %s, %s, %s, %s)",
                   (cd_data['name'], cd_data['artist_id'], cd_data['release_date'], cd_data['genre'], cd_data['price']))
    conn.commit()
    conn.close()

def update_cd(cd_id, cd_data):
    """Actualiza los datos de un CD en la base de datos"""
    conn = dbConnect()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE cds
        SET name = %s, artist_id = %s, release_date = %s, genre = %s, price = %s
        WHERE id = %s
    """, (cd_data['name'], cd_data['artist_id'], cd_data['release_date'], cd_data['genre'], cd_data['price'], cd_id))
    conn.commit()
    conn.close()

def delete_cd(cd_id):
    """Elimina un CD de la base de datos"""
    conn = dbConnect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cds WHERE id = %s", (cd_id,))
    conn.commit()
    conn.close()

def get_cds_by_name(name):
    connection = dbConnect()
    cursor = connection.cursor()
    query = "SELECT * FROM cds WHERE name LIKE %s"
    cursor.execute(query, ('%' + name + '%',))
    result = cursor.fetchall()
    connection.close()
    return result