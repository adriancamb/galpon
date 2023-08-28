
'''

categorias = [(1, 'Jardín', 'productos/jardin.html', 'img/imagen.jpg', 'Acá encontrá todo lo que necesitas para tu jardín'), (2, 'Parrillas', 'productos/parrillas.html', 'img/imagen.jpg', 'Esta es la descripción')]
subcategorias = [(1, 'Arrollamangueras', 'productos/arrollamangueras.html', 'img/arrollamanguera.jpg', 'Arrollamanguera de distintos tipos', 1, '', 1),
    (2, 'Bebederos', 'productos/bebederos.html', 'img/imagen.jpg', 'Esta es la descripcion', 1, '', 1),
    (3, 'Llamadores', 'productos/llamadores.html', 'img/imagen.jpg', 'Esta es la descripcion', 1, '', 1),
    (4, 'Veletas', 'productos/veletas.html', 'img/imagen.jpg', 'Esta es la descripcion', 0, '', 1),
    (5, 'Muebles de Jardín', 'productos/muebles-de-jardin.html', 'img/imagen.jpg', 'Esta es la descripcion', 0, '', 1),
    (6, 'Fundición de aluminio', 'productos/fundicion-de-aluminio.html', 'img/imagen.jpg', 'Esta es la descripcion', 0, 5, 1),
    (7, 'Función de hierro', 'productos/funcion-de-hierro.html', 'img/imagen.jpg', 'Esta es la descripcion', 0, 5, 1),
    (8, 'Hierro forjado', 'productos/hierro-forjado.html', 'img/imagen.jpg', 'Esta es la descripcion', 0, 5, 1),
    (9, 'Accesorios para parrillas', 'productos/accesorios-para-parrillas.html', 'img/imagen.jpg', 'Esta es la descripcion', 0, '', 2)]
'''
categorias = [(1, 'Jar', 'pro', 'img', 'Acá'),
              (2, 'Par', 'pro', 'img', 'Est')]

subcategorias = [(1, 'Arr', 'pro', 'img', 'Arr', 0, '', 1),
                 (2, 'Beb', 'pro', 'img', 'Est', 0, '', 1),
                 (3, 'Fun', 'pro', 'img', 'Est', 0, 2, 1),
                 (4, 'Fun', 'pro', 'img', 'Est', 0, 2, 1),
                 (5, 'Acc', 'pro', 'img', 'Est.', 0, '', 2)]
categorias_dict = {}

# Creamos el diccionario de categorías y sus subcategorías vacías
for categoria in categorias:
    categoria_id = categoria[0]
    categoria_nombre = categoria[1]
    categoria_subcategorias = []
    categorias_dict[categoria_id] = {
        "nombre": categoria_nombre, "subcategorias": categoria_subcategorias}

# Iteramos por las subcategorías para agregarlas a sus respectivas categorías
for subcategoria in subcategorias:
    subcategoria_id = subcategoria[0]
    subcategoria_nombre = subcategoria[1]
    subcategoria_subcategoria_id = subcategoria[6]
    subcategoria_categoria_id = subcategoria[7]

    # Si la categoría padre no existe en el diccionario, la creamos vacía
    if subcategoria_categoria_id not in categorias_dict:
        categorias_dict[subcategoria_categoria_id] = {
            "nombre": "", "subcategorias": []}

    # Buscamos la subcategoría padre en el diccionario de categorías
    subcategoria_padre = None
    for categoria in categorias_dict.values():
        for subcat in categoria["subcategorias"]:
            if subcat["nombre"] == subcategoria_nombre:
                subcategoria_padre = subcat
                break

    # Si la subcategoría padre no existe en el diccionario de categorías, la creamos vacía
    if subcategoria_padre is None:
        subcategoria_padre = {
            "nombre": subcategoria_nombre, "sub_subcategorias": {}}
        categorias_dict[subcategoria_categoria_id]["subcategorias"].append(
            subcategoria_padre)

    # Creamos la subcategoría actual y la agregamos a su subcategoría padre correspondiente
    subcategoria_actual = {
        "nombre": subcategoria_nombre, "sub_subcategorias": {}}
    if subcategoria_subcategoria_id not in subcategoria_padre["sub_subcategorias"]:
        subcategoria_padre["sub_subcategorias"][subcategoria_subcategoria_id] = []
    subcategoria_padre["sub_subcategorias"][subcategoria_subcategoria_id].append(
        subcategoria_actual)

# Creamos el código HTML a partir del diccionario de
print(categorias_dict)

html = '<ul class="navbar-nav col-lg-6 justify-content-lg-center">'

for categoria_id, categoria in categorias_dict.items():
    html += f'<li class="nav-item dropdown">'
    html += f'<a class="nav-link dropdown-toggle" href="productos/{categoria["nombre"].lower()}.html" data-bs-toggle="dropdown" aria-expanded="false">{categoria["nombre"]}</a>'
    if categoria['subcategorias']:
        html += '<ul class="dropdown-menu">'
        for subcategoria in categoria['subcategorias']:
            html += f'<li class="dropdown-submenu"><a class="dropdown-item dropdown-toggle" href="#">{subcategoria["nombre"]}</a>'
            if subcategoria['sub_subcategorias']:
                html += '<ul class="dropdown-menu">'
                for sub_subcategoria_id, sub_subcategorias in subcategoria['sub_subcategorias'].items():
                    html += f'<li class="dropdown-submenu"><a class="dropdown-item dropdown-toggle" href="#">Subcategoría {sub_subcategoria_id}</a>'
                    html += '<ul class="dropdown-menu">'
                    for sub_subcategoria in sub_subcategorias:
                        html += f'<li><a class="dropdown-item" href="productos/{sub_subcategoria["nombre"].lower()}.html">{sub_subcategoria["nombre"]}</a></li>'
                    html += '</ul>'
                    html += '</li>'
            if subcategoria['subcategorias']:
                html += '<ul class="dropdown-menu">'
                for sub_subcategoria in subcategoria['subcategorias']:
                    html += f'<li><a class="dropdown-item" href="productos/{sub_subcategoria["nombre"].lower()}.html">{sub_subcategoria["nombre"]}</a></li>'
                html += '</ul>'
            html += '</li>'
        html += '</ul>'
    html += '</li>'

html += '</ul>'

# print(html)


'''

<ul class="navbar-nav col-lg-6 justify-content-lg-center">
                <li class="nav-item dropdown"><a class="nav-link dropdown-toggle" href="productos/jardín.html"
                    data-bs-toggle="dropdown" aria-expanded="false">Jardín</a>
                  <ul class="dropdown-menu">
                    <li><a class="dropdown-item" href="productos/arrollamangueras.html">Arrollamangueras</a>
                      <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="productos/arrollamangueras.html">Arrollamangueras</a></li>
                      </ul>
                    </li>
                    <li><a class="dropdown-item" href="productos/bebederos.html">Bebederos</a>
                      <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="productos/bebederos.html">Bebederos</a></li>
                      </ul>
                    </li>
                    <li><a class="dropdown-item" href="productos/llamadores.html">Llamadores</a>
                      <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="productos/llamadores.html">Llamadores</a></li>
                      </ul>
                    </li>
                    <li><a class="dropdown-item" href="productos/veletas.html">Veletas</a>
                      <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="productos/veletas.html">Veletas</a></li>
                      </ul>
                    </li>
                    <li><a class="dropdown-item" href="productos/muebles de jardín.html">Muebles de Jardín</a>
                      <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="productos/muebles de jardín.html">Muebles de Jardín</a></li>
                      </ul>
                    </li>
                    <li><a class="dropdown-item" href="productos/fundición de aluminio.html">Fundición de aluminio</a>
                      <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="productos/fundición de aluminio.html">Fundición de
                            aluminio</a></li>
                      </ul>
                    </li>
                    <li><a class="dropdown-item" href="productos/función de hierro.html">Función de hierro</a>
                      <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="productos/función de hierro.html">Función de hierro</a></li>
                      </ul>
                    </li>
                    <li><a class="dropdown-item" href="productos/hierro forjado.html">Hierro forjado</a>
                      <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="productos/hierro forjado.html">Hierro forjado</a></li>
                      </ul>
                    </li>
                  </ul>
                </li>
                <li class="nav-item dropdown"><a class="nav-link dropdown-toggle" href="productos/parrillas.html"
                    data-bs-toggle="dropdown" aria-expanded="false">Parrillas</a>
                  <ul class="dropdown-menu">
                    <li><a class="dropdown-item" href="productos/accesorios para parrillas.html">Accesorios para
                        parrillas</a>
                      <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="productos/accesorios para parrillas.html">Accesorios para parrillas</a></li>
                      </ul>
                    </li>
                  </ul>
                </li>
              </ul>













              <li class="nav-item dropdown"><a class="nav-link dropdown-toggle" href="productos/jardin.html"
                  data-bs-toggle="dropdown" aria-expanded="false">Jardín</a>
                <ul class="dropdown-menu">
                  <li><a class="dropdown-item" href="productos/arrollamangueras.html">Arrollamangueras</a></li>
                  <li><a class="dropdown-item" href="productos/bebederos.html">Bebederos</a></li>
                  <li><a class="dropdown-item" href="productos/llamadores.html">Llamadores</a></li>
                  <li><a class="dropdown-item" href="productos/veletas.html">Veletas</a></li>
                  <li class="dropdown-submenu"><a class="dropdown-item" href="muebles-de-jardin.html">Muebles de
                      Jardín</a>
                    <ul class="dropdown-menu dropdown-submenu">
                      <li><a class="dropdown-item" href="fundicion-de-aluminio.html">Fundición de aluminio</a></li>
                      <li><a class="dropdown-item" href="funcion-de-hierro.html">Función de hierro</a></li>
                      <li><a class="dropdown-item" href="hierro-forjado.html">Hierro forjado</a></li>
                    </ul>
                  </li>
                </ul>
              </li>
              <li class="nav-item dropdown"><a class="nav-link dropdown-toggle" href="productos/parrillas.html"
                  data-bs-toggle="dropdown" aria-expanded="false">Parrillas</a>
                <ul class="dropdown-menu">
                  <li><a class="dropdown-item" href="accesorios-para-parrillas.html">Accesorios para parrillas</a></li>
                </ul>
              </li>
            </ul>









'''
