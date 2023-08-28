import sqlite3
import json

# Abrir una conexión con la base de datos
conn = sqlite3.connect('categorias.db')

# Crear una tabla para las categorías
conn.execute('''
    CREATE TABLE if not exists categorias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        url TEXT,
        imagen TEXT,
        descripcion TEXT
    )
''')

# Crear una tabla para las subcategorías
conn.execute('''
    CREATE TABLE if not exists subcategorias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        url TEXT,
        imagen TEXT,
        descripcion TEXT,
        destacado INTEGER,
        categoria_id INTEGER,
        FOREIGN KEY(categoria_id) REFERENCES categorias(id)
    )
''')

# Crear una tabla para las sub-subcategorías
conn.execute('''
    CREATE TABLE if not exists sub_subcategorias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        url TEXT,
        imagen TEXT,
        descripcion TEXT,
        destacado INTEGER,
        categoria_id INTEGER,
        subcategoria_id INTEGER,
        FOREIGN KEY(categoria_id) REFERENCES categorias(id),
        FOREIGN KEY(subcategoria_id) REFERENCES subcategorias(id)
    )
''')

# Leer el JSON y cargar los datos en la base de datos
with open('datos.json', 'r') as f:
    data = json.load(f)

for categoria in data['categorias']:
    # Insertar la categoría y obtener su ID
    categoria_id = conn.execute('''
        INSERT INTO categorias (nombre, url, imagen, descripcion)
        VALUES (?, ?, ?, ?)
    ''', (categoria['nombre'], categoria['url'], categoria['imagen'], categoria['descripcion'])).lastrowid

    for subcategoria in categoria.get('subcategorias', []):

        # Insertar la subcategoría y obtener su ID
        subcategoria_id = conn.execute('''
            INSERT INTO subcategorias (nombre, url, imagen, descripcion, destacado, categoria_id)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (subcategoria['nombre'], subcategoria['url'], subcategoria['imagen'], subcategoria['descripcion'], subcategoria.get('destacado'), categoria_id)).lastrowid

        for sub_subcategoria in subcategoria.get('subcategorias', []):
            # Insertar la sub-subcategoría
            conn.execute('''
                INSERT INTO sub_subcategorias (nombre, url, imagen, descripcion, destacado, categoria_id, subcategoria_id)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (sub_subcategoria['nombre'], sub_subcategoria['url'], sub_subcategoria['imagen'], sub_subcategoria['descripcion'], sub_subcategoria.get('destacado'), categoria_id, subcategoria_id))

# Cerrar la conexión
conn.commit()
conn.close()
