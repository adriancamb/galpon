import json
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect('galpon.db')
cursor = conn.cursor()

# Crear las tablas en SQLite
cursor.execute('''
    CREATE TABLE IF NOT EXISTS subcategorias (
        id           INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre       TEXT    NOT NULL,
        url          TEXT    NOT NULL,
        imagen       TEXT    NOT NULL,
        descripcion  TEXT,
        destacado    INTEGER DEFAULT 0,
        id_padre     INTEGER,
        id_categoria INTEGER REFERENCES categorias (id),
        FOREIGN KEY (
            id_padre
        )
        REFERENCES subcategorias (id)
    );
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS categorias (
        id          INTEGER PRIMARY KEY,
        nombre      TEXT,
        url         TEXT,
        imagen      TEXT,
        descripcion TEXT
    );
''')

# Leer el archivo JSON
with open('categorias.json') as file:
    data = json.load(file)

# Insertar datos en la tabla de categorías
for categoria in data['categorias']:
    cursor.execute('''
        INSERT INTO categorias (nombre, url, imagen, descripcion)
        VALUES (?, ?, ?, ?)
    ''', (categoria['nombre'], categoria['url'], categoria['imagen'], categoria['descripcion']))

    # Insertar datos en la tabla de subcategorías
    for subcategoria in categoria['subproductos']:
        if 'subproductos' in subcategoria:
            # Si la subcategoría tiene subproductos, primero se inserta la subcategoría y luego los subproductos
            cursor.execute('''
                INSERT INTO subcategorias (nombre, url, imagen, descripcion, destacado, id_padre, id_categoria)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (subcategoria['nombre'], subcategoria['url'], subcategoria['imagen'], subcategoria['descripcion'], subcategoria['destacado'], None, categoria['id']))

            id_padre = cursor.lastrowid

            for subproducto in subcategoria['subproductos']:
                cursor.execute('''
                    INSERT INTO subcategorias (nombre, url, imagen, descripcion, destacado, id_padre, id_categoria)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (subproducto['nombre'], subproducto['url'], subproducto['imagen'], subproducto['descripcion'], subproducto['destacado'], id_padre, categoria['id']))
        else:
            # Si la subcategoría no tiene subproductos, se inserta directamente en la tabla de subcategorías
            cursor.execute('''
                INSERT INTO subcategorias (nombre, url, imagen, descripcion, destacado, id_padre, id_categoria)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (subcategoria['nombre'], subcategoria['url'], subcategoria['imagen'], subcategoria['descripcion'], subcategoria['destacado'], None, categoria['id']))

# Guardar cambios en la base de datos
conn.commit()

# Cerrar conexión a la base de datos
conn.close()

