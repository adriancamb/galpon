import sqlite3

# Conectarse a la base de datos
conn = sqlite3.connect('galpon.db')

# Ejecutar una consulta SQL para obtener los datos
cursor = conn.cursor()
cursor.execute('SELECT * FROM categorias')

  # Obtener los resultados y generar los elementos HTML
contenedor = '<ul class="navbar-nav col-lg-6 justify-content-lg-center>'
for categoria in cursor.fetchall():
    # Crear el elemento li para la categoría
    itemCategoria = '<li class="nav-item dropdown">'

    # Crear el elemento a para la categoría
    linkCategoria = f'<a class="nav-link dropdown-toggle" href="{categoria[1]}" data-bs-toggle="dropdown" aria-expanded="false">{categoria[0]}</a>'

    # Crear la lista de productos para la categoría
    listaProductos = '<ul class="dropdown-menu">'
    cursor.execute(
        f'SELECT * FROM productos WHERE categoria_id={categoria[2]}')
    for producto in cursor.fetchall():
        itemLista = f'<li><a class="dropdown-item" href="{producto[1]}">{producto[0]}</a></li>'
        listaProductos += itemLista
    listaProductos += '</ul>'

    # Agregar los elementos a la página
    itemCategoria += linkCategoria + listaProductos + '</li>'
    contenedor += itemCategoria
contenedor += '</ul>'

# Cerrar la conexión a la base de datos
conn.close()
