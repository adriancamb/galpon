




''''''

import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('E:/Adrián/Documentos/Argentina programa 4.0/PaginaGalpon/prueba/galpon.db')
cursor = conn.cursor()
#cursor.execute('PRAGMA encoding="UTF-8";')
# Consulta SQL para obtener las categorías y subcategorías
query = """
    SELECT c.nombre as categoria, c.url as url_categoria, s.nombre as subcategoria, s.url as url_subcategoria,
           s2.nombre as subcategoria2, s2.url as url_subcategoria2, s3.nombre as subcategoria3, s3.url as url_subcategoria3,
           s4.nombre as subcategoria4, s4.url as url_subcategoria4
    FROM categorias c
    INNER JOIN subcategorias s ON c.id = s.id_categoria
    LEFT JOIN subcategorias2 s2 ON s.id = s2.id_subcategoria
    LEFT JOIN subcategorias3 s3 ON s2.id = s3.id_subcategoria2
    LEFT JOIN subcategorias4 s4 ON s3.id = s4.id_subcategoria3
"""

# Ejecución de la consulta SQL
cursor.execute(query)
resultados = cursor.fetchall()
print(resultados)

# Generación de la lista HTML
html = ''
categorias_previas = set()
subcategorias_previas = [None, None, None, None]
categoria_actual =""
subcategoria2_actual = ""
for categoria, url_categoria, subcategoria, url_subcategoria, subcategoria2, url_subcategoria2, subcategoria3, url_subcategoria3, subcategoria4, url_subcategoria4 in resultados:
    if categoria:

        if categoria not in categorias_previas:
            html += f'<li class="nav-item dropdown"><a class="nav-link dropdown-toggle" href="{url_categoria}" data-bs-toggle="dropdown" aria-expanded="false">{categoria}</a>\n'
            html += '    <ul class="dropdown-menu">\n' 
            categoria_actual == categoria
        if not subcategoria2:
            html += f'<li><a class="dropdown-item" href="{url_subcategoria}">{subcategoria}</a></li>'
        elif subcategoria2_actual == "":
            html += f'<li class="dropdown-submenu"><a class="dropdown-item" href="{url_subcategoria}">{subcategoria}</a>\n'
            html += f'  <ul class="dropdown-menu dropdown-submenu">\n'
            subcategoria2_actual = subcategoria2
       # elif :
        #    html += f'<li><a class="dropdown-item" href="{url_subcategoria2}">{subcategoria2}</a></li>\n'

        '''# Si la subcategoría ha cambiado, abrir el submenú nuevo
        if subcategoria and subcategoria != subcategorias_previas[0]:
            html += f'        <li><a class="dropdown-item" href="{url_subcategoria}">{subcategoria}</a></li>\n'
            #html += '            <ul class="dropdown-menu dropdown-submenu">\n'
        if subcategoria2 and subcategoria2 != subcategorias_previas[1]:
            html += f'                <li><a class="dropdown-item" href="{url_subcategoria2}">{subcategoria2}</a>\n'
            html += '                    <ul class="dropdown-menu dropdown-submenu">\n'
        if subcategoria3 and subcategoria3 != subcategorias_previas[2]:
            html += f'                        <li><a class="dropdown-item" href="{url_subcategoria3}">{subcategoria3}</a>\n'
            html += '                            <ul class="dropdown-menu dropdown-submenu">\n'
        if subcategoria4 and subcategoria4 != subcategorias_previas[3]:
            html += f'                                <li><a class="dropdown-item" href="{url_subcategoria4}">{subcategoria4}</a></li>\n'
        '''# Recordar las categorías y subcategorías previas para la próxima iteración
        categorias_previas.add(categoria)
        subcategorias_previas = [subcategoria, subcategoria2, subcategoria3, subcategoria4]

# Cerrar el último submenú
if subcategoria4:
    html
    html += '                        </ul>\n'
    html += '                    </li>\n'
if subcategoria3:
    html += '                </ul>\n'
    html += '            </li>\n'
if subcategoria2:
    html += '            </ul>\n'
    html += '        </li>\n'
if subcategoria:
    html += '        </ul>\n'
    html += '    </li>\n'
html += '</ul>'

conn.close()
print(html)

                    




for categoria, url_categoria, subcategoria, url_subcategoria, subcategoria2, url_subcategoria2, subcategoria3, url_subcategoria3, subcategoria4, url_subcategoria4 in resultados:
    if categoria:
        # Si la categoría ha cambiado, cerrar el submenú anterior
        if categoria not in categorias_previas and categorias_previas:
            html += '    </ul>\n'
            html += '</li>\n'
        # Si la subcategoría ha cambiado, cerrar el submenú anterior
        if subcategoria and subcategoria != subcategorias_previas[0]:
            html += '            </ul>\n'
            html += '        </li>\n'
        if subcategoria2 and subcategoria2 != subcategorias_previas[1]:
            html += '                </ul>\n'
            html += '            </li>\n'
        if subcategoria3 and subcategoria3 != subcategorias_previas[2]:
            html += '                    </ul>\n'
            html += '                </li>\n'
        if subcategoria4 and subcategoria4 != subcategorias_previas[3]:
            html += '                        </ul>\n'
            html += '                    </li>\n'
        # Si la categoría ha cambiado, abrir el submenú nuevo
        if categoria not in categorias_previas:
            html += f'<li class="nav-item dropdown"><a class="nav-link dropdown-toggle" href="{url_categoria}" data-bs-toggle="dropdown" aria-expanded="false">{categoria}</a>\n'
            html += '    <ul class="dropdown-menu">\n'
        # Si la subcategoría ha cambiado, abrir el submenú nuevo
        if subcategoria and subcategoria != subcategorias_previas[0]:
            html += f'        <li><a class="dropdown-item" href="{url_subcategoria}">{subcategoria}</a></li>\n'
            #html += '            <ul class="dropdown-menu dropdown-submenu">\n'
        if subcategoria2 and subcategoria2 != subcategorias_previas[1]:
            html += f'                <li><a class="dropdown-item" href="{url_subcategoria2}">{subcategoria2}</a>\n'
            html += '                    <ul class="dropdown-menu dropdown-submenu">\n'
        if subcategoria3 and subcategoria3 != subcategorias_previas[2]:
            html += f'                        <li><a class="dropdown-item" href="{url_subcategoria3}">{subcategoria3}</a>\n'
            html += '                            <ul class="dropdown-menu dropdown-submenu">\n'
        if subcategoria4 and subcategoria4 != subcategorias_previas[3]:
            html += f'                                <li><a class="dropdown-item" href="{url_subcategoria4}">{subcategoria4}</a></li>\n'
        # Recordar las categorías y subcategorías previas para la próxima iteración
        categorias_previas.add(categoria)
        subcategorias_previas = [subcategoria, subcategoria2, subcategoria3, subcategoria4]

# Cerrar el último submenú
if subcategoria4:
    html
    html += '                        </ul>\n'
    html += '                    </li>\n'
if subcategoria3:
    html += '                </ul>\n'
    html += '            </li>\n'
if subcategoria2:
    html += '            </ul>\n'
    html += '        </li>\n'
if subcategoria:
    html += '        </ul>\n'
    html += '    </li>\n'
html += '</ul>'












'''

import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('galpon.db')
cursor = conn.cursor()

# Consulta SQL para obtener las categorías y subcategorías
query = """
    SELECT c.nombre as categoria, c.url as url_categoria, s.nombre as subcategoria, s.url as url_subcategoria,
           s2.nombre as subcategoria2, s2.url as url_subcategoria2, s3.nombre as subcategoria3, s3.url as url_subcategoria3,
           s4.nombre as subcategoria4, s4.url as url_subcategoria4
    FROM categorias c
    LEFT JOIN subcategorias s ON c.id = s.id_categoria
    LEFT JOIN subcategorias2 s2 ON s.id = s2.id_subcategoria
    LEFT JOIN subcategorias3 s3 ON s2.id = s3.id_subcategoria2
    LEFT JOIN subcategorias4 s4 ON s3.id = s4.id_subcategoria3
"""

# Ejecución de la consulta SQL
cursor.execute(query)
resultados = cursor.fetchall()

# Generación de la lista HTML
html = '<ul class="dropdown-menu dropdown-submenu">\n'
for fila in resultados:
    categoria, url_categoria, subcategoria, url_subcategoria, subcategoria2, url_subcategoria2, subcategoria3, url_subcategoria3, subcategoria4, url_subcategoria4 = fila
    if categoria:
        html += f'<li class="dropdown-submenu"><a href="{url_categoria}">{categoria}</a>\n'
    if subcategoria:
        html += f'<ul class="dropdown-menu"><li><a href="{url_subcategoria}">{subcategoria}</a>\n'
    if subcategoria2:
        html += f'<ul class="dropdown-menu"><li><a href="{url_subcategoria2}">{subcategoria2}</a>\n'
    if subcategoria3:
        html += f'<ul class="dropdown-menu"><li><a href="{url_subcategoria3}">{subcategoria3}</a>\n'
    if subcategoria4:
        html += f'<ul class="dropdown-menu"><li><a href="{url_subcategoria4}">{subcategoria4}</a>\n'
    html += '</li></ul>\n'
html += '</ul>'

# Cierre de la conexión a la base de datos
conn.close()

# Impresión de la lista HTML
print(html)

'''




