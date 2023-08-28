
import sqlite3

# Crear conexión con la base de datos
conn = sqlite3.connect('productos\categorias.db')

# Crear un cursor para interactuar con la base de datos
cur = conn.cursor()

# Obtener todas las categorías principales
cur.execute("SELECT * FROM categorias WHERE id_padre IS NULL")
categorias_principales = cur.fetchall()

cur.execute("select distinct id_padre from categorias where id_padre NOT IN (select id from categorias where id_padre is NULL)")
id_padres = cur.fetchall()
id_subcategorias = [tupla[0] for tupla in id_padres]

# Función recursiva para generar el HTML de las subcategorías
def generar_subcategorias(id_padre):
    cur.execute("SELECT * FROM categorias WHERE id_padre = ?", (id_padre,))
    subcategorias = cur.fetchall()

    # Si no hay subcategorías, retornar una cadena vacía
    if not subcategorias:
        return ""
    

    #select id from categorias where id_padre is NULL;
    #me devuelve los id de las categorias principales: 1 10  16  18 21

    '''
    select * from categorias where id_padre NOT IN (select id from categorias where id_padre is NULL);
    
id  nombre                 id_padre  descripcion
--  ---------------------  --------  ---------------------------------------------------------
7   Fundición de aluminio  6         Esta es la descripcion
8   Función de hierro      6         Esta es la descripcion
9   Hierro forjado         6         Esta es la descripcion
24  Enlonzadas             23        cacerolas-de-fundicion-enlozadas
25  Sin enlonzar           23        cacerolas-de-fundicion-sin-enlozar
26  Ovaladas               25        cacerolas-de-fundicion-sin-enlozar-ovaladas
27  Doble función          26        cacerolas-de-fundicion-sin-enlozar-ovaladas-doble-funcion
29  Lisas                  28        planchas-para-bifes-lisas
30  Rayadas                28        planchas-para-bifes-rayadas
31  Enlonzadas             30        planchas-para-bifes-rayadas-enlozadas
32  Sin enlonzar           30        planchas-para-bifes-rayadas-sin-enlozar
34  Mangos de madera       33        provoleteras-mango-de-madera
35  Enlonzadas             34        provoleteras-enlozadas
36  Sin enlonzar           34        provoleteras-sin-enlozar
37  Mangos de fundicion    33        provoleteras-mango-de-fundicion
38  Enlonzadas             37        provoleteras-enlozadas
39  Sin enlonzar           37        provoleteras-sin-enlozar
40  De 15 porciones        33        provoleteras-15-porciones
41  Enlonzadas             40        provoleteras-15-porciones-enlozadas
42  Sin enlonzar           40        provoleteras-15-porciones-sin-enlozar
45  Enlonzadas             44        paelleras-con-2-asas-enlozadas
46  Sin enlonzar           44        paelleras-con-2-asas-sin-enlozar
48  Enlonzados             47        woks-enlozados
49  Sin enlonzar           47        woks-sin-enlozar
    
    
    me devuelve los registros que son subcategorias de alguna categoria que no son las principales
    
    <li class="dropdown-submenu"><a class="dropdown-item" href="muebles-de-jardin.html">Muebles de Jardín</a>
      <ul class="dropdown-menu dropdown-submenu">
    '''
    
    # Generar el HTML para las subcategorías
    html = "<ul class='dropdown-menu'>" #tendria que meterlo dentro del for siguiente
    
    for subcategoria in subcategorias:
        # Generar el HTML para las subcategorías
        #if subcategoria[6] == 0:#si es una categoria principal
        #    html = "<ul class='dropdown-menu'>" 
        #print(html)
        if subcategoria[0] in id_subcategorias:
            html += '<li class="dropdown-submenu">'
        else:
            html += '<li>'
        #print(html)
        # Si la subcategoría tiene subcategorías hijas, agregar la clase "dropdown-item"
        if generar_subcategorias(subcategoria[0]):
            html += "<a class='dropdown-item' href='{}'>{}</a>".format(
                    
                subcategoria[2], subcategoria[1]
            )
            html += generar_subcategorias(subcategoria[0])
            #print(html)
        # Si la subcategoría no tiene subcategorías hijas, agregar solo un enlace
        else:
            html += "<a class='dropdown-item' href='{}'>{}</a>".format(subcategoria[2], subcategoria[1])
            #print(html)
        html += "</li>"  # Usamos el salto de línea en sí mismo
    html += "</ul>"
 
    return html

# Generar el HTML para las categorías principales
html_categorias = ""
for categoria in categorias_principales:
    html_categorias += "<li class='nav-item dropdown'>"
    #print(html_categorias)
    # Si la categoría tiene subcategorías hijas, agregar la clase "dropdown"
    if generar_subcategorias(categoria[0]):
        html_categorias += "<a class='nav-link dropdown-toggle' href='{}' data-bs-toggle='dropdown' aria-expanded='false'>{}</a>".format(
            categoria[2], categoria[1]
        )
        #print(html_categorias)
        html_categorias += generar_subcategorias(categoria[0])
    # Si la categoría no tiene subcategorías hijas, agregar solo un enlace
    else:
        html_categorias += "<a class='nav-link' href='{}'>{}</a>".format(categoria[2], categoria[1])
    html_categorias += "</li>"

# Generar el HTML completo para el menú de navegación
#html_menu = "<ul class='navbar-nav me-auto mb-2 mb-lg-0'>{}</ul>".format(html_categorias)
html_menu = "{}".format(html_categorias)

# Imprimir el resultado

print(html_menu)





