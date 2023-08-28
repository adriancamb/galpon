document.addEventListener('DOMContentLoaded', function() {
  
    // Obtiene el nombre del archivo HTML actual
   var currentFile = window.location.pathname.split('/').pop();
   console.log("currentFile:", currentFile)
   // Remueve la extensión ".html" del nombre del archivo y Reemplaza los guiones ("-") por espacios en el nombre de la categoría
   var nombreCategoria = currentFile.slice(0, -5).replace(/-/g, ' ');
   const titulo = document.getElementById('pagina-titulo');
   titulo.textContent = nombreCategoria;

 });
async function obtenerCategoriaDesdeURL() {
    try {
        const response = await fetch('/productos/categorias.json');
        const data = await response.json();

        const rutaActual = window.location.pathname;

        const indiceUltimaBarra = rutaActual.lastIndexOf("/");
        //esta es la ruta de la categoria que se obtiene desde el producto
        const rutaCategoriaObtenida = rutaActual.substring(0, indiceUltimaBarra) + ".html";
        
        var currentFile = rutaCategoriaObtenida.split('/').pop();
        var nombreCategoria = currentFile.slice(0, -5).replace(/-/g, ' ');
        console.log("nombreCategoria:", nombreCategoria)
        
        mostrarVistasMiniatura(nombreCategoria);

    } catch (error) {
        console.error('Error al cargar el archivo JSON:', error);
        return null;
    }
}

