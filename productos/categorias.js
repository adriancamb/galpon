// Lee el archivo json
fetch('../productos/categorias.json')
  .then(response => response.json())
  .then(data => {
    // Busca el contenedor donde se insertarán los items
    const contenedor = document.getElementById("json");

    // Genera los items para cada categoría
    data.categorias.forEach(categoria => {
      // Crea el elemento li para la categoría
      const itemCategoria = document.createElement('li');
      itemCategoria.classList.add('nav-item', 'dropdown');

      // Crea el elemento a para la categoría
      const linkCategoria = document.createElement('a');
      linkCategoria.classList.add('nav-link', 'dropdown-toggle');
      linkCategoria.href = '#';
      linkCategoria.dataset.bsToggle = 'dropdown';
      linkCategoria.setAttribute('aria-expanded', 'false');
      linkCategoria.textContent = categoria.nombre;

      // Crea la lista de items para la categoría
      const listaItems = document.createElement('ul');
      listaItems.classList.add('dropdown-menu');

      // Genera los items para la categoría
      categoria.items.forEach(item => {
        const itemLista = document.createElement('li');
        const linkItem = document.createElement('a');
        linkItem.classList.add('dropdown-item');
        linkItem.href = '#';
        linkItem.textContent = item.nombre;

        itemLista.appendChild(linkItem);
        listaItems.appendChild(itemLista);
      });

      // Agrega los elementos a la página
      itemCategoria.appendChild(linkCategoria);
      itemCategoria.appendChild(listaItems);
      contenedor.appendChild(itemCategoria);
    });
  });