
// Leer el archivo JSON de productos
fetch("./productos/categorias.json")
  .then(response => response.json())
  .then(data => {
    // Filtrar solo los productos destacados
    const productosDestacados = data.categorias.reduce((acc, categoria) => {
      const productos = categoria.productos.filter(producto => Boolean(producto.destacado));
      return acc.concat(productos);
    }, []);

    // Crear el HTML para cada producto destacado
    const productosHTML = productosDestacados.map(producto => `
      <div class="col-sm-4">
        <div class="card">
          <img src="${producto.imagen}" class="card-img-top" alt="Imagen de ${producto.nombre}">
          <div class="card-body">
            <div class="cardTexto">
              <h5 class="card-title">${producto.nombre}</h5>
              <p class="card-text">${producto.descripcion}</p>
            </div>
            <div class= "masInfo">
              <a href="${producto.url}" class="btn btn-warning" style="float: center";>Más información</a>
            </div>
          </div>
        </div>
      </div>
    `).join('');

    // Agregar el HTML de los productos destacados al contenedor
    document.getElementById('productos-container').innerHTML = ` <div class="row">${productosHTML}</div> `;
  });
