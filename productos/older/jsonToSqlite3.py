1. Primero, instala la biblioteca sqlite3 si aún no está instalada.
2. A continuación, crea un archivo Python y pega el siguiente código:

```python
import json
import sqlite3

# Reemplaza esto con tu JSON
json_data = '''
[
    {
        "id": 1,
        "nombre": "Juan",
        "edad": 30
    },
    {
        "id": 2,
        "nombre": "Maria",
        "edad": 25
    }
]
'''

# Convierte el JSON en una lista de diccionarios
data = json.loads(json_data)

# Conecta a la base de datos SQLite (o crea una si no existe)
conn = sqlite3.connect("../productos/productos.json")
cursor = conn.cursor()

# Crea la tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS personas (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    edad INTEGER
)
""")

# Inserta los datos en la tabla
for item in data:
    cursor.execute("""
    INSERT INTO personas (id, nombre, edad) VALUES (?, ?, ?)
    """, (item['id'], item['nombre'], item['edad']))

# Guarda los cambios y cierra la conexión
conn.commit()
conn.close()
```

3. Reemplaza el `json_data` en el código con el JSON que deseas convertir.
4. Ejecuta el archivo Python y se creará una base de datos SQLite con los datos del JSON.