//document.addEventListener('DOMContentLoaded', function() { tengo que usarlo porque si no se carga el dom primero, no
//me encuentra el id 'pagina-titulo'
document.addEventListener('DOMContentLoaded', function() {
  
   // Obtiene el nombre del archivo HTML actual
  var currentFile = window.location.pathname.split('/').pop();
  //console.log("currentFile:", currentFile)
  // Remueve la extensión ".html" del nombre del archivo y Reemplaza los guiones ("-") por espacios en el nombre de la categoría
  var nombreCategoria = currentFile.slice(0, -5).replace(/-/g, ' ');
  const titulo = document.getElementById('pagina-titulo');
  titulo.textContent = nombreCategoria;
  console.log("nombreCategoria:", nombreCategoria)
  // Llama a la función mostrarVistasMiniatura y pasa el nombre de la categoría
  mostrarVistasMiniatura(nombreCategoria);
  
 
});