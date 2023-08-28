import sqlite3

# crea una conexión a la base de datos
conn = sqlite3.connect('categorias.db')

# crea un cursor para interactuar con la base de datos
c = conn.cursor()

# crea la tabla de categorías
c.execute('''CREATE TABLE categorias
             (id INTEGER PRIMARY KEY,
              nombre TEXT,
              url TEXT,
              imagen TEXT)''')

# crea la tabla de subcategorías
c.execute('''CREATE TABLE subcategorias
             (id INTEGER PRIMARY KEY,
              nombre TEXT,
              url TEXT,
              imagen TEXT,
              id_categoria INTEGER,
              id_subcategoria_padre INTEGER,
              FOREIGN KEY (id_categoria) REFERENCES categorias(id),
              FOREIGN KEY (id_subcategoria_padre) REFERENCES subcategorias(id))''')

# agrega los datos de categorías
categorias_data = [
    ("Jardín", "productos/jardin.html", "img/imagen.jpg"),
    ("Gastronomía", "productos/gastronomia.html", "img/imagen.jpg"),
]

for categoria in categorias_data:
    c.execute("INSERT INTO categorias (nombre, url, imagen) VALUES (?, ?, ?)", categoria)

# agrega los datos de subcategorías
subcategorias_data = [
    ("Arrollamangueras", "productos/arrollamangueras.html", "img/arrollamanguera.jpg", 1, None),
    ("Muebles de Jardín", "muebles-de-jardin.html", "img/imagen.jpg", 1, None),
    ("Calderos en hierro", "calderos-en-hierro.html", "img/imagen.jpg", 2, None),
    ("Cacerolas de fundición", "cacerolas-de-fundicion.html", "img/imagen.jpg", 2, None),
    ("Enlozadas", "productos/enlozadas.html", "img/imagen.jpg", 2, 4),
    ("Sin enlozar", "productos/enlozadas.html", "img/imagen.jpg", 2, 4),
    ("Ovaladas", "productos/ovaladas.html", "img/imagen.jpg", 2, 6),
    ("Doble función", "doble-funcion.html", "img/imagen.jpg", 2, 7)
]

for subcategoria in subcategorias_data:
    c.execute("INSERT INTO subcategorias (nombre, url, imagen, id_categoria, id_subcategoria_padre) VALUES (?, ?, ?, ?, ?)", subcategoria)

# guarda los cambios y cierra la conexión
conn.commit()
conn.close()
