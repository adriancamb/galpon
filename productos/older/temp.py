html = ""

categorias = [(1, 'Jardín', 'productos/jardin.html', 'img/imagen.jpg', 'Acá encontrá todo lo que necesitas para tu jardín'), (2, 'Parrillas', 'productos/parrillas.html', 'img/imagen.jpg', 'Esta es la descripción'), (3, 'Calefacción', 'productos/calefaccion.html', 'img/imagen.jpg', 'Esta es la descripción'), (4, 'Iluminacion', 'productos/iluminacion.html', 'img/imagen.jpg', 'Esta es la descripción'), (5, 'Gastronomia', 'productos/gastronomia.html', 'img/imagen.jpg', 'Esta es la descripción')]
subcategorias = [(1, 'Arrollamangueras', 'productos/arrollamangueras.html', 'img/arrollamanguera.jpg', 'Arrollamanguera de distintos tipos', 1, '', 1),
    (2, 'Bebederos', 'productos/bebederos.html', 'img/imagen.jpg', 'Esta es la descripcion', 1, '', 1),
    (3, 'Llamadores', 'productos/llamadores.html', 'img/imagen.jpg', 'Esta es la descripcion', 1, '', 1),
    (4, 'Veletas', 'productos/veletas.html', 'img/imagen.jpg', 'Esta es la descripcion', 0, '', 1),
    (5, 'Muebles de Jardín', 'productos/muebles-de-jardin.html', 'img/imagen.jpg', 'Esta es la descripcion', 0, '', 1),
    (6, 'Fundición de aluminio', 'productos/fundicion-de-aluminio.html', 'img/imagen.jpg', 'Esta es la descripcion', 0, 5, 1),
    (7, 'Función de hierro', 'productos/funcion-de-hierro.html', 'img/imagen.jpg', 'Esta es la descripcion', 0, 5, 1),
    (8, 'Hierro forjado', 'productos/hierro-forjado.html', 'img/imagen.jpg', 'Esta es la descripcion', 0, 5, 1),
    (9, 'Accesorios para parrillas', 'productos/accesorios-para-parrillas.html', 'img/imagen.jpg', 'Esta es la descripcion', 0, '', 2),
    (10, 'Asadores', 'productos/asadores.html', 'img/imagen.jpg', 'Esta es la descripcion', 0, '', 2),
    (11, 'Herrajes', 'productos/herrajes.html', 'img/imagen.jpg', 'Esta es la descripcion', 0, '', 2),
    (12, 'Parrillas a carbón o leña', 'productos/parrillas-a-carbon-o-lena.html', 'img/imagen.jpg', 'Esta es la descripcion', 0, '', 2),
    (13, 'Parrillas a gas', 'productos/parrillas-a-gas.html', 'img/imagen.jpg', 'Esta es la descripcion', 0, '', 2),
    (14, 'Hogares', 'productos/hogares.html', 'img/imagen.jpg', 'Esta es la descripción', 0, '', 3),
    (15, 'Faroles', 'productos/faroles.html', 'img/imagen.jpg', 'Esta es la descripción', 0, '', 4),
    (16, 'Faroles con columnas', 'productos/faroles-con-columnas.html', 'img/imagen.jpg', 'Esta es la descripción', 0, '', 4),
    (17, 'Calderos en hierro', 'productos/calderos-en-hierro.html', 'img/calderos-en-hierro.jpg', 'calderos-en-hierro', 0, '', 5),
    (18, 'Calcerolas de fundicion', 'productos/cacerolas-de-fundicion.html', 'img/cacerolas-de-fundicion.jpg', 'cacerolas-de-fundicion', 0, '', 5),
    (19, 'Enlonzadas', 'productos/cacerolas-de-fundicion-enlonzadas.html', 'img/cacerolas-de-fundicion-enlonzadas.jpg', 'cacerolas-de-fundicion-enlozadas', 0, 18, 5),
    (20, 'Sin enlonzar', 'productos/cacerolas-de-fundicion-sin-enlonzar.html', 'img/cacerolas-de-fundicion-sin-enlonzar.jpg', 'cacerolas-de-fundicion-sin-enlozar', 0, 18, 5),
    (21, 'Ovaladas', 'productos/cacerolas-de-fundicion-sin-enlonzar-ovaladas.html', 'img/cacerolas-de-fundicion-sin-enlonzar-ovaladas.jpg', 'cacerolas-de-fundicion-sin-enlozar-ovaladas', 0, 20, 5),
    (22, 'Doble función', 'productos/cacerolas-de-fundicion-sin-enlonzar-ovaladas-doble-funcion.html', 'img/cacerolas-de-fundicion-sin-enlonzar-ovaladas-doble-funcion.jpg', 'cacerolas-de-fundicion-sin-enlozar-ovaladas-doble-funcion', 0, 21, 5),
    (23, 'Planchas para bifes', 'productos/planchas-para-bifes.html', 'img/planchas-para-bifes.jpg', 'planchas-para-bifes', 0, '', 5),
    (24, 'Lisas', 'productos/planchas-para-bifes-lisas.html', 'img/planchas-para-bifes-lisas.jpg', 'planchas-para-bifes-lisas', 0, 23, 5),
    (25, 'Rayadas', 'productos/planchas-para-bifes-rayadas.html', 'img/planchas-para-bifes-rayadas.jpg', 'planchas-para-bifes-rayadas', 0, 23, 5),
    (26, 'Enlonzadas', 'productos/planchas-para-bifes-rayadas-enlozadas.html', 'img/planchas-para-bifes-rayadas-enlozadas.jpg', 'planchas-para-bifes-rayadas-enlozadas', 0, 25, 5),
    (27, 'Sin enlonzar', 'productos/planchas-para-bifes-rayadas-sin-enlozar.html', 'img/planchas-para-bifes-rayadas-sin-enlozar.jpg', 'planchas-para-bifes-rayadas-sin-enlozar', 0, 25, 5),
    (28, 'Provoleteras de fundicion', 'productos/provoleteras.html', 'img/provoleteras.jpg', 'provoleteras', 0, 0, 5),
    (29, 'Mangos de madera', 'productos/provoleteras-mango-de-madera.html', 'img/provoleteras-mango-de-madera.jpg', 'provoleteras-mango-de-madera', 0, 28, 5),
    (30, 'Enlonzadas', 'productos/provoleteras-enlonzadas.html', 'img/provoleteras-enlonzadas.jpg', 'provoleteras-enlozadas', 0, 29, 5),
    (31, 'Sin enlonzar', 'productos/provoleteras-sin-enlonzar.html', 'img/provoleteras-sin-enlonzar.jpg', 'provoleteras-sin-enlozar', 0, 29, 5),
    (32, 'Mangos de fundicion', 'productos/provoleteras-mango-de-fundicion.html', 'img/provoleteras-mango-de-fundicion.jpg', 'provoleteras-mango-de-fundicion', 0, 28, 5),     
    (33, 'Enlonzadas', 'productos/provoleteras-enlonzadas.html', 'img/provoleteras-enlonzadas.jpg', 'provoleteras-enlozadas', 0, 32, 5),
    (34, 'Sin enlonzar', 'productos/provoleteras-sin-enlonzar.html', 'img/provoleteras-sin-enlonzar.jpg', 'provoleteras-sin-enlozar', 0, 32, 5),
    (35, 'De 15 porciones', 'productos/provoleteras-15-porciones.html', 'img/provoleteras-15-porciones.jpg', 'provoleteras-15-porciones', 0, 28, 5),
    (36, 'Enlonzadas', 'productos/provoleteras-15-porciones-enlozadas.html', 'img/provoletera-15-porcioness-enlonzadas.jpg', 'provoleteras-15-porciones-enlozadas', 0, 35, 5), 
    (37, 'Sin enlonzar', 'productos/provoleteras-15-porciones-sin-enlonzar.html', 'img/provoleteras-15-porciones-sin-enlonzar.jpg', 'provoleteras-15-porciones-sin-enlozar', 0, 35, 5),
    (38, 'Asaderas en chapa plegada', 'productos/asaderas-en-chapa-plegada.html', 'img/asaderas-en-chapa-plegada.jpg', 'asaderas-en-chapa-plegada', 0, '', 5),
    (39, 'Paelleras con 2 asas', 'productos/paelleras-con-2-asas.html', 'img/paelleras-con-2-asas.jpg', 'paelleras-con-2-asas', 0, '', 5),
    (40, 'Enlonzadas', 'productos/paelleras-con-2-asas-enlozadas.html', 'img/paelleras-con-2-asas-enlonzadas.jpg', 'paelleras-con-2-asas-enlozadas', 0, 39, 5),
    (41, 'Sin enlonzar', 'productos/paelleras-con-2-asas-sin-enlonzar.html', 'img/paelleras-con-2-asas-sin-enlonzar.jpg', 'paelleras-con-2-asas-sin-enlozar', 0, 39, 5),       
    (42, 'Woks', 'productos/woks.html', 'img/woks.jpg', 'woks', 0, '', 5),
    (43, 'Enlonzados', 'productos/woks-enlozados.html', 'img/woks-enlonzados.jpg', 'woks-enlozados', 0, 42, 5),
    (44, 'Sin enlonzar', 'productos/woks-sin-enlonzar.html', 'img/woks-sin-enlonzar.jpg', 'woks-sin-enlozar', 0, 42, 5),
    (45, 'Sartén mango de planchuela', 'productos/sarten-mango-de-planchuela.html', 'img/sarten-mango-de-planchuela.jpg', 'sarten-mango-de-planchuela', 0, None, 5),
    (46, 'Pizzera en chapa enlozada', 'productos/pizzera-en-chapa-enlozada.html', 'img/pizzera-en-chapa-enlozada.jpg', 'pizzera-en-chapa-enlozada', 0, None, 5)]


# Crear un diccionario con las categorías y sus respectivas subcategorías
categorias_dict = {}
for categoria in categorias:
    categorias_dict[categoria[0]] = {'nombre': categoria[1], 'subcategorias': []}

for subcategoria in subcategorias:
    categoria_id_padre = subcategoria[6]
    if categoria_id_padre in categorias_dict:
        categorias_dict[categoria_id_padre]['subcategorias'].append(subcategoria)

# Crear la estructura de HTML utilizando los datos del diccionario
html = '<ul class="navbar-nav col-lg-6 justify-content-lg-center">'
for categoria_id, categoria in categorias_dict.items():
    html += f'<li class="nav-item dropdown">'
    html += f'<a class="nav-link dropdown-toggle" href="productos/{categoria["nombre"].lower()}.html" data-bs-toggle="dropdown" aria-expanded="false">{categoria["nombre"]}</a>'
    if categoria['subcategorias']:
        html += '<ul class="dropdown-menu">'
        for subcategoria in categoria['subcategorias']:
            html += f'<li><a class="dropdown-item" href="productos/{subcategoria[1].lower()}.html">{subcategoria[1]}</a></li>'
        html += '</ul>'
    html += '</li>'
html += '</ul>'

print(html)


'''
subcategorias = [(1, 'Jardin1', 'prod14', 'img14', 'Desc14', 1, '', 1),
(2, 'Jardin1a', 'prod15', 'img15', 'Desc15', 1, 1, 1),
(3, 'Jardin1b', 'prod16', 'img16', 'Desc16', 1, 1, 1),
(4, 'parrilla1', 'prod17', 'img17', 'Desc17', 0, '', 2),
(5, 'calefaccion1', 'prod18', 'img18', 'Desc18', 0, '', 3),
(6, 'calefaccion1a', 'prod19', 'img19', 'Desc19', 0, 5, 3)]
id_actual = 0
for cat in categorias:
    html += '<li class="nav-item dropdown"><a class="nav-link dropdown-toggle" href="' + cat[2] + '" data-bs-toggle="dropdown"aria-expanded="false">' + cat[1] + '</a>' + "\n" + '<ul class="dropdown-menu">'
    for subcat in subcategorias: #recorro todas las subcategorias
        id_actual = subcat[0]
        subcat_anterior = subcat
        
        if subcat[7] == cat[0]: #si la subcategoria es igual a la categoria actual
           if subcat[6] != "" or subcat[6] != None:     #si no es una sub subcategoria
              html += '<li><a class="dropdown-item" href="' + subcat[2] + '">' + subcat[1] + '</a></li>'
          # elif subcat[6] == id_actual:                 #si ES una sub subcategoria de la actual
               



print (html)

for elemento in subcategorias:
    if elemento[6] != "":
        for elemento2 in subcategorias:
            if elemento2[0] == elemento[6]:
                print (elemento2[1] + " " + elemento[1])
                '''