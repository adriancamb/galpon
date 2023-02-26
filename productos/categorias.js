// Lee el archivo json
fetch('../productos/categorias.json')
  .then(response => response.json())
  .then(data => {
    // Busca el contenedor donde se insertarán los productos
    const contenedor = document.getElementById("json");

    // Genera los productos para cada categoría
    data.categorias.forEach(categoria => {
      // Crea el elemento li para la categoría
      const itemCategoria = document.createElement('li');
      itemCategoria.classList.add('nav-item', 'dropdown');

      // Crea el elemento a para la categoría
      const linkCategoria = document.createElement('a');
      linkCategoria.classList.add('nav-link', 'dropdown-toggle');
      linkCategoria.href = categoria.url;
      linkCategoria.dataset.bsToggle = 'dropdown';
      linkCategoria.setAttribute('aria-expanded', 'false');
      linkCategoria.textContent = categoria.nombre;

      // Crea la lista de productos para la categoría
      const listaproductos = document.createElement('ul');
      listaproductos.classList.add('dropdown-menu');

      // Genera los productos para la categoría
      categoria.productos.forEach(item => {
        const itemLista = document.createElement('li');
        const linkItem = document.createElement('a');
        linkItem.classList.add('dropdown-item');
        linkItem.href = item.url;
        linkItem.textContent = item.nombre;

        itemLista.appendChild(linkItem);
        listaproductos.appendChild(itemLista);
      });


      // Agrega los elementos a la página
      itemCategoria.appendChild(linkCategoria);
      itemCategoria.appendChild(listaproductos);
      contenedor.appendChild(itemCategoria);
    });
  });






  const fs = require('fs');
const categorias = require('./categorias.json');

categorias.categorias.forEach(categoria => {
  const html = `
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="utf-8">
        <title>${categoria.nombre}</title>
      </head>
      <body>
        <h1>${categoria.nombre}</h1>
        <table>
          <thead>
            <tr>
              <th>Producto</th>
              <th>Precio</th>
            </tr>
          </thead>
          <tbody>
            ${categoria.productos.map(producto => `
              <tr>
                <td>${producto.nombre}</td>
                <td>${producto.precio}</td>
              </tr>
            `).join('')}
          </tbody>
        </table>
      </body>
    </html>
  `;
  fs.writeFileSync(categoria.url, html);
});
