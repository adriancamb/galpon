/*
para generar automáticamente las páginas con los productos desde el JSON

node generarHTML.js

*/

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
  fs.writeFileSync(`${categoria.url}.html`, html);
});
