import sqlite3

# Abrir la conexión con la base de datos
db = sqlite3.connect('E:\Adrián\Documentos\Argentina programa 4.0\PaginaGalpon\Prueba2\database.sqlite')

# Función recursiva para obtener las subcategorías
def obtenerSubcategorias(padre_id):
    query = f"SELECT * FROM categorias WHERE padre_id = {padre_id} ORDER BY izquierda"
    result = db.execute(query)

    subcategorias = []
    for row in result:
        subcategoria = {
            'id': row[0],
            'nombre': row[1],
            'url': row[2],
            'imagen': row[3],
            'subcategorias': obtenerSubcategorias(row[0])
        }
        subcategorias.append(subcategoria)

    return subcategorias

# Función recursiva para crear el HTML del menú
def crearMenuHTML(categorias):
    menuHTML = ''
    for categoria in categorias:
        menuHTML += '<li class="nav-item">'
        if len(categoria['subcategorias']) > 0:
            menuHTML += '<div class="dropdown">'
            menuHTML += f'<a class="nav-link dropdown-toggle" href="{categoria["url"]}" id="{categoria["nombre"].lower()}-dropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">{categoria["nombre"]}</a>'
            menuHTML += '<ul class="dropdown-menu" aria-labelledby="{categoria["nombre"].lower()}-dropdown">'
            menuHTML += crearMenuHTML(categoria['subcategorias'])
            menuHTML += '</ul></div>'
        else:
            menuHTML += f'<a class="nav-link" href="{categoria["url"]}">{categoria["nombre"]}</a>'
        menuHTML += '</li>'

    return menuHTML

# Obtener las categorías principales
query = "SELECT c1.nombre, c1.url, c2.nombre, c2.url FROM categorias c1 LEFT JOIN categorias c2 ON c2.padre_id = c1.id WHERE c1.padre_id IS NULL ORDER BY c1.izquierda, c2.izquierda;"
result = db.execute(query)

# Crear la estructura de árbol de categorías
categorias = []
for row in result:
    categoria = {
        'id': row[0],
        'nombre': row[1],
        'url': row[2],
        'imagen': row[3],
        'subcategorias': obtenerSubcategorias(row[0])
    }
    categorias.append(categoria)

# Crear el HTML del menú
menuHTML = crearMenuHTML(categorias)

# Imprimir el HTML del menú
print(menuHTML)
