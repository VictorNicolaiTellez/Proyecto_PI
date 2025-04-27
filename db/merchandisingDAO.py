# db/merchandisingDAO.py
from .dbconnection import connection

def get_all_merch():
    """Obtiene todo el merchandising"""
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM merchandising")
    merch = cursor.fetchall()
    cursor.close()
    return merch

def get_merch_by_id(merch_id):
    """Obtiene merchandising por ID"""
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM merchandising WHERE id = %s", (merch_id,))
    merch = cursor.fetchone()
    cursor.close()
    return merch

def add_merch(merch_data):
    """Agrega un nuevo artículo de merchandising a la base de datos"""
    
    cursor = connection.cursor()
    cursor.execute("INSERT INTO merchandising (name, type, price, stock) VALUES (%s, %s, %s, %s)",
                   (merch_data['name'], merch_data['type'], merch_data['price'], merch_data['stock']))
    connection.commit()
    cursor.close()

def update_merch(merch_id, merch_data):
    """Actualiza los datos de un artículo de merchandising"""
    
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE merchandising
        SET name = %s, type = %s, price = %s, stock = %s
        WHERE id = %s
    """, (merch_data['name'], merch_data['type'], merch_data['price'], merch_data['stock'], merch_id))
    connection.commit()
    cursor.close()

def delete_merch(merch_id):
    """Elimina un artículo de merchandising"""
    
    cursor = connection.cursor()
    cursor.execute("DELETE FROM merchandising WHERE id = %s", (merch_id,))
    connection.commit()
    cursor.close()

def get_merchandising_by_name(name):

    cursor = connection.cursor()
    query = "SELECT * FROM merchandising WHERE name LIKE %s"
    cursor.execute(query, ('%' + name + '%',))
    result = cursor.fetchall()
    cursor.close()
    return result