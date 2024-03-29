const quitaTildes = (str) => {
    return str.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
  };
  
  async function mostrarVistasMiniatura(nombreCategoria) {
    try {
        const response = await fetch('/productos/productos.json');
        const data = await response.json();
        const { id: idCategoriaObtenida, ruta: rutaCategoriaObtenida } = await obtenerIdCategoria(nombreCategoria);

        const rutaCategoriaElement = document.getElementById('ruta-categoria');
        const categorias = rutaCategoriaObtenida.split('/');
        const enlaces = categorias.map((categoria, index) => {
            const rutaParcial = categorias  
                .slice(0, index + 1)
                .join('/')
                .replace(/ /g, '-')
                .replace(/[áÁ]/g, "a")
                .replace(/[éÉ]/g, "e")
                .replace(/[íÍ]/g, "i")
                .replace(/[óÓ]/g, "o")
                .replace(/[úÚ]/g, "u")
                .replace(/[ñÑ]/g, "n")
                .replace(/[üÜ]/g, "u");
            const enlace = `<a href="/productos/Categorias/${rutaParcial}.html">${quitaTildes(categoria)}</a>`;
            return enlace;
        });

        rutaCategoriaElement.innerHTML = enlaces.slice(0, -1).join(' <i class="bi bi-arrow-right"></i> ') + enlaces[enlaces.length - 1];

        const subcategoriasFiltradas = data.filter(function (categoria) {
            const idCategoriaPadre = categoria.id_categoria_padre;
            return idCategoriaPadre === idCategoriaObtenida;
        });

        if (subcategoriasFiltradas.length > 0) {
            const contenedorProductos = document.getElementById('contenedor-productos');
            contenedorProductos.innerHTML = '';
            contenedorProductos.classList.add('contenedor-productos');

            subcategoriasFiltradas.forEach(function (categoria) {
                const vistaMiniatura = document.createElement('div');
                vistaMiniatura.className = 'vista-miniatura';

                const contenido =
                    '<a href="' + categoria.url + '">' +
                    '<img src="' + categoria.imagen + '" alt="' + categoria.nombre + '">' +
                    '</a>' +
                    '<h3><a href="' + categoria.url + '">' + categoria.nombre + '</a></h3>' +
                    '<p>' + categoria.descripcion_reducida + '</p>';
                vistaMiniatura.innerHTML = contenido;
                contenedorProductos.appendChild(vistaMiniatura);
            });
        } else {
            // Si no hay subcategorías, muestra los productos filtrados
            const productosFiltrados = data.filter(function (producto) {
                const idCategoriaProducto = producto.id_categoria;
                return idCategoriaProducto === idCategoriaObtenida;
            });

            const contenedorProductos = document.getElementById('contenedor-productos');
            contenedorProductos.innerHTML = '';
            contenedorProductos.classList.add('contenedor-productos');

            productosFiltrados.forEach(function (producto) {
                const vistaMiniatura = document.createElement('div');
                vistaMiniatura.className = 'vista-miniatura';

                const contenido =
                    '<a href="' + producto.url + '">' +
                    '<img src="' + producto.imagen + '" alt="' + producto.nombre + '">' +
                    '</a>' +
                    '<h3><a href="' + producto.url + '">' + producto.nombre + '</a></h3>' +
                    '<p>' + producto.descripcion_reducida + '</p>' +
                    '<h4>$' + producto.precio + '</h4>' +
                    '<button type="button" class="btn btn-primary"><i class="bi bi-cart-plus"></i></button>';
                vistaMiniatura.innerHTML = contenido;
                contenedorProductos.appendChild(vistaMiniatura);
            });
        }
    } catch (error) {
        console.error('Error al cargar el archivo JSON:', error);
    }
}
  
  async function obtenerIdCategoria(nombreCategoria) {
    try {
      const response = await fetch('/productos/categorias.json');
      const data = await response.json();
      const categoriasPrincipales = data.categorias;
  
      function buscarIdCategoria(obj, nombreCategoria, ruta = '') {
        if (Array.isArray(obj)) {
          for (let item of obj) {
            const id = buscarIdCategoria(item, nombreCategoria, ruta);
            if (id) {
              return id;
            }
          }
        } else if (typeof obj === 'object') {
          for (let key in obj) {
            if (key === 'nombre') {
              const nombre = obj[key];
              const nombreSeparado = nombre.split(' ').join('-'); // Reemplaza espacios por "-"
              if (nombre.toLowerCase() === nombreCategoria.toLowerCase() || nombreSeparado.toLowerCase() === nombreCategoria.toLowerCase()) {
                return {
                  id: obj['id'],
                  ruta: ruta + nombre + '/'
                };
              }
            }
            const id = buscarIdCategoria(obj[key], nombreCategoria, ruta + obj['nombre'] + '/');
            if (id) {
              return id;
            }
          }
        }
        return null; // Si no se encuentra ninguna coincidencia
      }
  
      const idCategoriaObtenida = buscarIdCategoria(categoriasPrincipales, nombreCategoria);
      return idCategoriaObtenida;
    } catch (error) {
      console.error('Error al cargar el archivo JSON:', error);
      return 0;
    }
  }
  /*
  function buscarCategoriaEnArreglo(arreglo, nombreCategoria) {
    return arreglo.find(function(categoria) {
      return categoria.nombre === nombreCategoria;
    });
  }
  */
  /*
  function buscarIdCategoriaRecursivo(categorias, nombreCategoria) {
    for (let i = 0; i < categorias.length; i++) {
      const categoria = categorias[i];
      const productos = categoria.productos;
      console.log ("productos:",productos)
      if (productos) {
        const subcategoriaEncontrada = buscarCategoriaEnArreglo(productos, nombreCategoria);
        if (subcategoriaEncontrada) {
          return subcategoriaEncontrada.id;
        }
  
        const idCategoria = buscarIdCategoriaRecursivo(productos, nombreCategoria);
        if (idCategoria !== 0) {
          return idCategoria;
        }
      }
  
      const subproductos = categoria.subproductos;
      if (subproductos) {
        const idCategoria = buscarIdCategoriaRecursivo(subproductos, nombreCategoria);
        if (idCategoria !== 0) {
          return idCategoria;
        }
      }
    }
  
    return 0;
  }
  */
