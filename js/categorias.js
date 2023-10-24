// Lee el archivo json
fetch('/productos/categorias.json')
  .then(response => response.json())
  .then(data => {
    // Busca el contenedor donde se insertarán los productos
    const contenedor = document.getElementById("json");

    // Genera los productos para cada categoría
    data.categorias.forEach(categoria => {
      // Crea el elemento li para la categoría
      const itemCategoria = document.createElement('li');
      itemCategoria.classList.add('nav-item', 'dropdown', 'hover-dropdown');

      // Crea el elemento a para la categoría
      const linkCategoria = document.createElement('a');
      linkCategoria.classList.add('nav-link', 'dropdown-toggle');
      linkCategoria.href = categoria.url;
      linkCategoria.dataset.bsToggle = 'dropdown';
      linkCategoria.setAttribute('aria-expanded', 'false');
      linkCategoria.textContent = categoria.nombre_corto;

      // Crea la lista de productos para la categoría
      const listaproductos = document.createElement('ul');
      listaproductos.classList.add('dropdown-menu');

      // Genera los productos para la categoría
      categoria.productos.forEach(item => {
        const itemLista = document.createElement('li');
        const linkItem = document.createElement('a');
        linkItem.classList.add('dropdown-item');
        linkItem.href = item.url;
        linkItem.textContent = item.nombre_corto;
        linkItem.setAttribute('target', '_self'); // Agrega el atributo target

        itemLista.appendChild(linkItem);
        listaproductos.appendChild(itemLista);

        // Agrega los subproductos para el producto actual
        if (item.subproductos) {
          const subproductosLista = document.createElement('ul');
          subproductosLista.classList.add('dropdown-menu', 'dropdown-submenu');

          item.subproductos.forEach(subproducto => {
            const subproductoLista = document.createElement('li');
            const subproductoLink = document.createElement('a');
            subproductoLink.classList.add('dropdown-item');
            subproductoLink.href = subproducto.url;
            subproductoLink.textContent = subproducto.nombre_corto;
            subproductoLink.setAttribute('target', '_self'); // Agrega el atributo target

            subproductoLista.appendChild(subproductoLink);

            // Agrega los sub-subproductos para el subproducto actual
            if (subproducto.subproductos) {
              const subsubproductosLista = document.createElement('ul');
              subsubproductosLista.classList.add('dropdown-menu', 'dropdown-submenu');

              subproducto.subproductos.forEach(subsubproducto => {
                const subsubproductoLista = document.createElement('li');
                const subsubproductoLink = document.createElement('a');
                subsubproductoLink.classList.add('dropdown-item');
                subsubproductoLink.href = subsubproducto.url;
                subsubproductoLink.textContent = subsubproducto.nombre_corto;
                subsubproductoLink.setAttribute('target', '_self'); // Agrega el atributo target

                subsubproductoLista.appendChild(subsubproductoLink);
                subsubproductosLista.appendChild(subsubproductoLista);
              });

              subproductoLista.classList.add('dropdown-submenu');
              subproductoLista.appendChild(subsubproductosLista);
            }

            subproductosLista.appendChild(subproductoLista);
          });

          itemLista.classList.add('dropdown-submenu');
          itemLista.appendChild(subproductosLista);
        }
      });

      // Agrega el evento de clic a la categoría principal
      linkCategoria.addEventListener('click', function (event) {
        event.preventDefault(); // Evita la acción predeterminada del enlace
        window.open(this.href, '_self'); // Abre el enlace en la misma pestaña
      });

      // Agrega los elementos a la página
      itemCategoria.appendChild(linkCategoria);
      itemCategoria.appendChild(listaproductos);
      contenedor.appendChild(itemCategoria);
    });

    // Agrega el código JavaScript para el despliegue al pasar el mouse por encima
    var dropdownItems = document.getElementsByClassName('hover-dropdown');
    for (var i = 0; i < dropdownItems.length; i++) {
      dropdownItems[i].addEventListener('mouseenter', function () {
        var dropdownMenu = this.querySelector('.dropdown-menu');
        dropdownMenu.classList.add('show');
      });

      dropdownItems[i].addEventListener('mouseleave', function () {
        var dropdownMenu = this.querySelector('.dropdown-menu');
        dropdownMenu.classList.remove('show');
      });
    }
  });





/*

fetch('../productos/categorias.json')
.then(response => response.json())
.then(data => {
const contenedor = document.getElementById("json");
data.categorias.forEach(categoria => {
const itemCategoria = document.createElement('li');
itemCategoria.classList.add('nav-item', 'dropdown');
const linkCategoria = document.createElement('a');
linkCategoria.classList.add('nav-link', 'dropdown-toggle');
linkCategoria.href = categoria.url;
linkCategoria.dataset.bsToggle = 'dropdown';
linkCategoria.setAttribute('aria-expanded', 'false');
linkCategoria.textContent = categoria.nombre;
const listaproductos = document.createElement('ul');
listaproductos.classList.add('dropdown-menu');
categoria.productos.forEach(item => {
const itemLista = document.createElement('li');
const linkItem = document.createElement('a');
linkItem.classList.add('dropdown-item');
linkItem.href = item.url;
linkItem.textContent = item.nombre;
itemLista.appendChild(linkItem);
listaproductos.appendChild(itemLista);
if (item.subproductos) {
const subproductosLista = document.createElement('ul');
subproductosLista.classList.add('dropdown-menu', 'dropdown-submenu');
item.subproductos.forEach(subproducto => {
const subproductoLista = document.createElement('li');
const subproductoLink = document.createElement('a');
subproductoLink.classList.add('dropdown-item');
subproductoLink.href = subproducto.url;
subproductoLink.textContent = subproducto.nombre;
subproductoLista.appendChild(subproductoLink);
if (subproducto.subproductos) {
const subsubproductosLista = document.createElement('ul');
subsubproductosLista.classList.add('dropdown-menu', 'dropdown-submenu');
subproducto.subproductos.forEach(subsubproducto => {
const subsubproductoLista = document.createElement('li');
const subsubproductoLink = document.createElement('a');
subsubproductoLink.classList.add('dropdown-item');
subsubproductoLink.href = subsubproducto.url;
subsubproductoLink.textContent = subsubproducto.nombre;
subsubproductoLista.appendChild(subsubproductoLink);
if (subsubproducto.subproductos) {
const subsubsubproductosLista = document.createElement('ul');
subsubsubproductosLista.classList.add('dropdown-menu', 'dropdown-submenu');
subsubproducto.subproductos.forEach(subsubsubproducto => {
const subsubsubproductoLista = document.createElement('li');
const subsubsubproductoLink = document.createElement('a');
subsubsubproductoLink.classList.add('dropdown-item');
subsubsubproductoLink.href = subsubsubproducto.url;
subsubsubproductoLink.textContent = subsubsubproducto.nombre;
subsubsubproductoLista.appendChild(subsubsubproductoLink);
subsubsubproductosLista.appendChild(subsubsubproductoLista);
});
subsubproductoLista.classList.add('dropdown-submenu');
subsubproductoLista.appendChild(subsubsubproductosLista);
}
subsubproductosLista.appendChild(subsubproductoLista);
});
subproductoLista.classList.add('dropdown-submenu');
subproductoLista.appendChild(subsubproductosLista);
}
subproductosLista.appendChild(subproductoLista);
});
itemLista.classList.add('dropdown-submenu');
itemLista.appendChild(subproductosLista);
}
});
itemCategoria.appendChild(linkCategoria);
itemCategoria.appendChild(listaproductos);
contenedor.appendChild(itemCategoria);
});
});
*/