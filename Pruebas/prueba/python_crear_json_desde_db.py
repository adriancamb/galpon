import sqlite3
import json

# Conectarse a la base de datos
conn = sqlite3.connect('galpon.db')
c = conn.cursor()

# Recuperar todas las categorías
c.execute('SELECT * FROM categorias')
categorias = []
for row in c.fetchall():
    categoria = {
        'nombre': row[1],
        'url': row[2],
        'imagen': row[3],
        'descripcion': row[4],
        'subcategorias': []
    }
    categorias.append(categoria)

    # Recuperar subcategorías para esta categoría
    c.execute('SELECT * FROM subcategorias WHERE categoria_id = ?', (row[0],))
    for sub_row in c.fetchall():
        subcategoria = {
            'nombre': sub_row[1],
            'url': sub_row[2],
            'imagen': sub_row[3],
            'descripcion': sub_row[4],
            'destacado': sub_row[5],
            'subcategorias': []
        }
        categoria['subcategorias'].append(subcategoria)

        # Recuperar sub subcategorías para esta subcategoría
        c.execute('SELECT * FROM sub_subcategorias WHERE subcategoria_id = ?', (sub_row[0],))
        for sub_sub_row in c.fetchall():
            sub_subcategoria = {
                'nombre': sub_sub_row[1],
                'url': sub_sub_row[2],
                'imagen': sub_sub_row[3],
                'descripcion': sub_sub_row[4],
                'destacado': sub_sub_row[5],
            }
            subcategoria['subcategorias'].append(sub_subcategoria)

# Generar el JSON
json_data = {'categorias': categorias}
json_string = json.dumps(json_data, indent=4)

# Imprimir el JSON generado
print(json_string)
