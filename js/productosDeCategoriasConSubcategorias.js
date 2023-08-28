var currentFile = window.location.pathname.split('/').pop();
var nombreCategoria = currentFile.slice(0, -5).replace(/-/g, ' ');

document.addEventListener('DOMContentLoaded', function() {
    // Obtiene el nombre del archivo HTML actual
    var currentFile = window.location.pathname.split('/').pop();
    // Remueve la extensión ".html" del nombre del archivo y Reemplaza los guiones ("-") por espacios en el nombre de la categoría
    var nombreCategoria = currentFile.slice(0, -5).replace(/-/g, ' ');
    const titulo = document.getElementById('pagina-titulo');
    titulo.textContent = nombreCategoria;
    main(nombreCategoria);

  });
/*
  const quitaTildes = (str) => {
    return str.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
  };
*/
  const contenedorProductos = document.getElementById('contenedor-productos');
  contenedorProductos.innerHTML = '';
  contenedorProductos.classList.add('contenedor-productos');

  function mostrarProducto(producto) {
//    console.log("producto:",quitaTildes(producto.nombre))
//    console.log("nombreCategoria:", nombreCategoria)
if (quitaTildes(producto.nombre) != nombreCategoria){
      const vistaMiniatura = document.createElement('div');
      vistaMiniatura.className = 'vista-miniatura';
      const contenido =
          '<a href="' + producto.url + '">' +
          '<img src="' + producto.imagen + '" alt="' + producto.nombre + '">' +
          '</a>' +
          '<h3><a href="' + producto.url + '">' + producto.nombre + '</a></h3>' +
          '<p>' + producto.descripcion + '</p>';
      vistaMiniatura.innerHTML = contenido;
      contenedorProductos.appendChild(vistaMiniatura);
    }
      if (producto.productos) {
        producto.productos.forEach(producto => {
            mostrarProducto(producto);
        });
    }
      if (producto.subproductos) {
          producto.subproductos.forEach(subproducto => {
              mostrarProducto(subproducto);
          });
      }
    }


  function findCategoryByName(categories, nombreBuscado) {

  //    console.log("nombreBuscado:", nombreBuscado)
      for (const category of categories) {
        nombreSinTilde = quitaTildes(category.nombre);
//        console.log("nombreSinTilde:", nombreSinTilde)
        
        //nombreSinTilde = quitaTildes(nombre);
          if (nombreSinTilde === nombreBuscado) {
  //            console.log("category.nombre:", category.nombre)
              return category;
          }
          if (category.productos) {
              const foundSubcategory = findCategoryByName(category.productos, nombreBuscado);
              if (foundSubcategory) {
                  return foundSubcategory;
              }
          }
          if (category.subproductos) {
              const foundSubcategory = findCategoryByName(category.subproductos, nombreBuscado);
              if (foundSubcategory) {
                  return foundSubcategory;
              }
          }
      }
      return undefined;
  }
  
  async function main(nombreCategoria) {

    
      const filePath = '/productos/categorias.json';
      const { id: idCategoriaObtenida, ruta: rutaCategoriaObtenida } = await obtenerIdCategoria(nombreCategoria);
  
      rutaCategoria(rutaCategoriaObtenida);
  
      try {
          const response = await fetch(filePath);
          const data = await response.json();
          const categorias = data.categorias;
  
          const nombreBuscado = nombreCategoria;

          const foundCategory = findCategoryByName(categorias, nombreBuscado);

  
          if (foundCategory) {
              mostrarProducto(foundCategory);
          } else {
              const mensajeError = document.createElement('p');
              mensajeError.textContent = 'Información no encontrada.';
              contenedorProductos.appendChild(mensajeError);
          }
      } catch (error) {
        console.error('Error al cargar el archivo JSON:', error);
      }
  }