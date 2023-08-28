import sqlite3
import json

# Conectar a la base de datos SQLite
conn = sqlite3.connect('productos/galpon.db')
cursor = conn.cursor()

# Ejecutar una consulta SQL para obtener todos los productos
cursor.execute('SELECT * FROM productos')
productos = cursor.fetchall()

# Obtener los nombres de las columnas
columnas = [desc[0] for desc in cursor.description]

# Crear una lista de diccionarios para representar los productos
lista_productos = []
for producto in productos:
    producto_dict = dict(zip(columnas, producto))
    lista_productos.append(producto_dict)

# Cerrar la conexión a la base de datos
conn.close()

# Escribir los datos en un archivo JSON
with open('productos/productos.json', 'w') as archivo_json:
    json.dump(lista_productos, archivo_json, indent=4)

