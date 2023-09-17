async function cargarCategoriasYProductos() {
    try {
      const response = await fetch('/productos/categorias.json'); // Asegúrate de que la ruta sea correcta
      const data = await response.json();
      const categoriasPrincipales = data.categorias;
  
      // Llama a la función para mostrar categorías y productos
      mostrarCategoriasYProductos(categoriasPrincipales);
    } catch (error) {
      console.error('Error al cargar el archivo JSON:', error);
    }
  }
  
  function mostrarCategoriasYProductos(categorias, contenedor) {
    const contenedorProductos = contenedor || document.getElementById('categorias-lista');

    categorias.forEach(function (categoria) {
        const contenedorCategoria = document.createElement('div');

        if (categoria.productos && categoria.productos.length > 0){
            contenedorCategoria.className = 'categorias-lista'; // Agrega una clase para el contenedor de categoría
        }
        if (categoria.subproductos && categoria.subproductos.length > 0){
          contenedorCategoria.className = 'categorias-lista'; // Agrega una clase para el contenedor de categoría
      }
        contenedorProductos.appendChild(contenedorCategoria);

        const vistaMiniatura = document.createElement('div');
        vistaMiniatura.className = 'vista-miniatura-ABM';

        const contenido = `
        <p>${categoria.id}: <span id="nombre-${categoria.id}">${categoria.nombre}</span>
            <input type="text" id="input-nombre-${categoria.id}" style="display: none;">
            <button onclick="editarCampo('nombre', ${categoria.id})">Editar</button>
            <button onclick="guardarCampo('nombre', ${categoria.id})" style="display: none;">Guardar</button>
        </p>
        <p>Descripción: <span id="descripcion-${categoria.id}">${categoria.descripcion}</span>
            <input type="text" id="input-descripcion-${categoria.id}" style="display: none;">
            <button onclick="editarCampo('descripcion', ${categoria.id})">Editar</button>
            <button onclick="guardarCampo('descripcion', ${categoria.id})" style="display: none;">Guardar</button>
        </p>
        <p>Imagen: <span id="imagen-${categoria.id}">${categoria.imagen}</span>
            <img src="${categoria.imagen}" alt="${categoria.nombre}">
            <input type="file" id="input-imagen-${categoria.id}" style="display: none;">
            <button onclick="editarCampo('imagen', ${categoria.id})">Editar</button>
            <button onclick="guardarCampo('imagen', ${categoria.id})" style="display: none;">Guardar</button>
        </p>
        <p>Destacado: <span id="destacado-${categoria.id}">${categoria.destacado}</span>
            <input type="checkbox" id="input-destacado-${categoria.id}" style="display: none;">
            <button onclick="editarCampo('destacado', ${categoria.id})">Editar</button>
            <button onclick="guardarCampo('destacado', ${categoria.id})" style="display: none;">Guardar</button>
        </p>
        `;

        vistaMiniatura.innerHTML = contenido;
        contenedorCategoria.appendChild(vistaMiniatura);

        if (categoria.productos && categoria.productos.length > 0) {
            mostrarCategoriasYProductos(categoria.productos, contenedorCategoria); // Llama recursivamente para los productos
        }

        if (categoria.subproductos && categoria.subproductos.length > 0) {
            mostrarCategoriasYProductos(categoria.subproductos, contenedorCategoria); // Llama recursivamente para los subproductos
        }
    });
}

  // Función para activar la edición de un campo
function editarCampo(campo, id) {
    const span = document.getElementById(`${campo}-${id}`);
    const input = document.getElementById(`input-${campo}-${id}`);
    const guardarBtn = document.querySelector(`button[onclick="guardarCampo('${campo}', ${id})"]`);
    const editarBtn = document.querySelector(`button[onclick="editarCampo('${campo}', ${id})"]`);
  
    // Mostrar el input y el botón "Guardar", ocultar el span y el botón "Editar"
    span.style.display = 'none';
    input.style.display = 'inline-block';
    guardarBtn.style.display = 'inline-block';
    editarBtn.style.display = 'none';
  
    // Poner el valor actual del campo en el input
    input.value = span.textContent;
  
    if (campo === 'destacado') {
      // Para el campo destacado, también necesitas manejar el estado del checkbox
      const checkbox = document.getElementById(`input-${campo}-${id}`);
      const valorActual = span.textContent === 'true'; // Convierte el texto en un valor booleano
      checkbox.checked = valorActual;
    }
  }
  
  // Función para guardar un campo editado
  function guardarCampo(campo, id) {
    const span = document.getElementById(`${campo}-${id}`);
    const input = document.getElementById(`input-${campo}-${id}`);
    const guardarBtn = document.querySelector(`button[onclick="guardarCampo('${campo}', ${id})"]`);
    const editarBtn = document.querySelector(`button[onclick="editarCampo('${campo}', ${id})"]`);
  
    // Actualizar el valor en el span con el valor del input
    span.textContent = input.value;
  
    // Ocultar el input y el botón "Guardar", mostrar el span y el botón "Editar"
    span.style.display = 'inline-block';
    input.style.display = 'none';
    guardarBtn.style.display = 'none';
    editarBtn.style.display = 'inline-block';
  
    if (campo === 'destacado') {
      // Para el campo destacado, también necesitas manejar el estado del checkbox
      const checkbox = document.getElementById(`input-${campo}-${id}`);
      span.textContent = checkbox.checked.toString(); // Convierte el valor booleano en texto
    }
  }
  
  // Llama a la función para cargar categorías y productos cuando sea necesario
  cargarCategoriasYProductos();
  
