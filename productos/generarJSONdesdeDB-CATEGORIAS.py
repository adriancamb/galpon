import sqlite3
import json

# Conectarse a la base de datos
conn = sqlite3.connect('productos/galpon.db')
c = conn.cursor()

# Leer los datos de la tabla
c.execute('SELECT id, nombre, url, imagen, id_padre, descripcion, destacado, nombre_corto FROM categorias')
categorias = c.fetchall()

# Función para buscar las subcategorías de una categoría
def buscar_subcategorias(id_padre):
    subcategorias = []
    for categoria in categorias:
        if categoria[4] == id_padre:
            subcategoria = {
                "id":categoria[0],
                "nombre": categoria[1],
                "url": categoria[2],
                "imagen": categoria[3],
                "descripcion": categoria[5],
                "destacado": bool(categoria[6]),
                "nombre_corto": categoria[7]
            }
            subcategorias_hijas = buscar_subcategorias(categoria[0])
            if subcategorias_hijas:
                subcategoria["subproductos"] = subcategorias_hijas
            subcategorias.append(subcategoria)
    return subcategorias

# Generar la estructura del JSON
json_data = {"categorias": []}
for categoria in categorias:
    if categoria[4] == None:
        nueva_categoria = {
            "id":categoria[0],
            "nombre": categoria[1],
            "url": categoria[2],
            "imagen": categoria[3],
            "descripcion": categoria[5],
            "destacado": bool(categoria[6]),
            "nombre_corto": categoria[7]
        }
        subcategorias = buscar_subcategorias(categoria[0])
        if subcategorias:
            nueva_categoria["productos"] = subcategorias
        json_data["categorias"].append(nueva_categoria)

# Convertir a JSON y guardar en archivo
#with open('productos/categoriasGPT.json', 'w', encoding='utf-8') as f:
with open('productos/categorias.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(json_data, ensure_ascii=False, indent=4).encode('utf8').decode())
    #json.dump(json_data, f, ensure_ascii=False, indent=4)