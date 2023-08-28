function generarAcordeones(data, parentElement) {
  data.categorias.forEach(function (categoria, index) {
      var categoriaItem = document.createElement('div');
      categoriaItem.className = 'accordion-item';

      var categoriaHeader = document.createElement('h2');
      categoriaHeader.className = 'accordion-header';

      var categoriaButton = document.createElement('button');
      categoriaButton.className = 'accordion-button collapsed btn btn-warning';
      categoriaButton.type = 'button';
      categoriaButton.setAttribute('data-bs-toggle', 'collapse');
      categoriaButton.setAttribute('data-bs-target', '#collapse_' + index);
      categoriaButton.setAttribute('aria-expanded', 'false');
      categoriaButton.setAttribute('aria-controls', 'collapse_' + index);
      categoriaButton.textContent = categoria.nombre;

      categoriaHeader.appendChild(categoriaButton);
      categoriaItem.appendChild(categoriaHeader);

      var categoriaCollapse = document.createElement('div');
      categoriaCollapse.id = 'collapse_' + index;
      categoriaCollapse.className = 'accordion-collapse collapse';
      categoriaCollapse.setAttribute('aria-labelledby', 'heading_' + index);
      categoriaCollapse.setAttribute('data-bs-parent', '#accordion');

      var categoriaBody = document.createElement('div');
      categoriaBody.className = 'accordion-body';
      /*
      var categoriaImage = document.createElement('img');
      categoriaImage.src = categoria.imagen;
      categoriaBody.appendChild(categoriaImage);
     
      var categoriaDescription = document.createElement('p');
      categoriaDescription.textContent = categoria.descripcion;
      categoriaBody.appendChild(categoriaDescription);
      */
      var categoriaList = document.createElement('ul');
      categoriaBody.appendChild(categoriaList);
      categoriaCollapse.appendChild(categoriaBody);
      categoriaItem.appendChild(categoriaCollapse);
      parentElement.appendChild(categoriaItem);

      if (categoria.subproductos) {
          generarSubproductos(categoria.subproductos, categoriaList);
      } else if (categoria.productos) {
          generarProductos(categoria.productos, categoriaList);
      }
  });
}

function generarSubproductos(subproductos, parentElement) {
  subproductos.forEach(function (subproducto, index) {
      var subproductoItem = document.createElement('li');
      var subproductoLink = document.createElement('a');
      subproductoLink.href = subproducto.url;
      subproductoLink.textContent = subproducto.nombre;
      subproductoItem.appendChild(subproductoLink);
      parentElement.appendChild(subproductoItem);

      if (subproducto.subproductos) {
          var subproductoList = document.createElement('ul');
          subproductoItem.appendChild(subproductoList);
          generarSubproductos(subproducto.subproductos, subproductoList);
      }
  });
}

function generarProductos(productos, parentElement) {
  productos.forEach(function (producto) {
      var productoItem = document.createElement('li');
      var productoLink = document.createElement('a');
      productoLink.href = producto.url;
      productoLink.textContent = producto.nombre;
      productoItem.appendChild(productoLink);
      parentElement.appendChild(productoItem);

      if (producto.subproductos) {
          var subproductoList = document.createElement('ul');
          productoItem.appendChild(subproductoList);
          generarSubproductos(producto.subproductos, subproductoList);
      }
  });
}               

fetch('/productos/categorias.json')
  .then(function (response) {
      return response.json();
  })
  .then(function (data) {
      var accordionContainer = document.getElementById('accordion');
      generarAcordeones(data, accordionContainer);
      //console.log(accordion.innerHTML);
      
  })
  .catch(function (error) {
      console.log(error);
  });