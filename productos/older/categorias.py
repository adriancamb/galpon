from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('./productos/galpon.db')

''' a continuacion la prueba de que abre bien la db
import os
import sqlite3

# establecer la ruta de la base de datos
db_path = "./productos/galpon.db"

# conectarse a la base de datos
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# imprimir la ruta de la base de datos
print("La base de datos se encuentra en:", os.path.abspath(db_path))

# ejecutar una consulta
cur.execute("SELECT * FROM categorias")
rows = cur.fetchall()

# imprimir los resultados
for row in rows:
    print(row)

# cerrar la conexión a la base de datos
conn.close()

 termina la prueba de que abre bien la db'''
    

@app.route('/categorias')
def categorias():
    with app.app_context():
        cur = conn.cursor()
        cur.execute('SELECT * FROM categorias')
        categorias = cur.fetchall()
        cur.execute('SELECT * FROM subcategorias')
        subcategorias = cur.fetchall()
        print (subcategorias)
        return render_template('categorias.html', categorias=categorias, subcategorias=subcategorias)


#if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=5000)
#    app.run(host='127.0.0.1', port=5500)

print (categorias)

def generar_menu(categorias):

    html = '<ul class="navbar-nav col-lg-6 justify-content-lg-center">\n'
    for categoria in categorias:
        html += f'<li class="nav-item dropdown"><a class="nav-link dropdown-toggle" href="{categoria["url"]}" data-bs-toggle="dropdown" aria-expanded="false">{categoria["nombre"]}</a>\n'
        if categoria['subcategorias']:
            html += '<ul class="dropdown-menu">\n'
            for subcategoria in categoria['subcategorias']:
                html += f'<li><a class="dropdown-item" href="{subcategoria["url"]}">{subcategoria["nombre"]}</a></li>\n'
                if subcategoria['subcategorias']:
                    html += '<li class="dropdown-submenu"><a class="dropdown-item" href="{subcategoria["url"]}">{subcategoria["nombre"]}</a>\n'
                    html += '<ul class="dropdown-menu dropdown-submenu">\n'
                    for subsubcategoria in subcategoria['subcategorias']:
                        html += f'<li><a class="dropdown-item" href="{subsubcategoria["url"]}">{subsubcategoria["nombre"]}</a></li>\n'
                    html += '</ul></li>\n'
            html += '</ul>'
        html += '</li>\n'
    html += '</ul>'
    return html

categorias = categorias()
html = generar_menu(categorias)