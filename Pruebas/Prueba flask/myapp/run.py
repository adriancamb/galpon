from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Configurar la conexión a la base de datos
def get_db_connection():
    conn = sqlite3.connect('db/menu.db')
    conn.row_factory = sqlite3.Row
    return conn

# Cerrar la conexión a la base de datos
def close_db_connection(conn):
    conn.close()

# Página de inicio que muestra el menú
@app.route('/')
def index():
    conn = get_db_connection()
    categories = conn.execute('SELECT * FROM categories WHERE parent_id IS NULL').fetchall()
    close_db_connection(conn)
    return render_template('index.html', categories=categories)

# Página que muestra los productos de una categoría
@app.route('/category/<int:id>')
def category(id):
    conn = get_db_connection()
    category = conn.execute('SELECT * FROM categories WHERE id = ?', (id,)).fetchone()
    subcategories = conn.execute('SELECT * FROM categories WHERE parent_id = ?', (id,)).fetchall()
    close_db_connection(conn)
    return render_template('category.html', category=category, subcategories=subcategories)

# Página que muestra los productos de una subcategoría
@app.route('/subcategory/<int:id>')
def subcategory(id):
    conn = get_db_connection()
    subcategory = conn.execute('SELECT * FROM categories WHERE id = ?', (id,)).fetchone()
    products = conn.execute('SELECT * FROM products WHERE subcategory_id = ?', (id,)).fetchall()
    close_db_connection(conn)
    return render_template('subcategory.html', subcategory=subcategory, products=products)

# Página que muestra los detalles de un producto
@app.route('/product/<int:id>')
def product(id):
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE id = ?', (id,)).fetchone()
    close_db_connection(conn)
    return render_template('product.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
