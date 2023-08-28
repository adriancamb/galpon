document.addEventListener("DOMContentLoaded", async function () {
  const productDetails = document.getElementById("product-details");
  const productImagen = document.getElementById("product-image");

  const productUrl = window.location.pathname;
  const product = await obtenerProductoYMostrarDetalles(productUrl);

  if (product) {

    const titulo = document.getElementById('pagina-titulo');
    titulo.textContent = product.nombre;
    
    //const titulo = document.getElementById('pagina-titulo');
    productImagen.src = product.imagen;
    productImagen.alt = product.descripcion_reducida;
    productDetails.innerHTML = productHtml;
      
    var productHtml = `
        <h1 class="mt-3">${product.nombre}</h1>
        <h2 class="text-success">$${product.precio}</h2>
        <p class="text-muted">Disponibilidad: ${product.cantidad} unidades</p>
        <div class="mt-4">
          <p>${product.descripcion}</p>
        </div>
        <button type="button" class="btn btn-primary"><i class="bi bi-cart-plus"></i></button>
      </div>
      `;
      productDetails.innerHTML = productHtml;
    }
});

async function obtenerProductoYMostrarDetalles(productUrl) {
  try {
    const response = await fetch("/productos/productos.json");
    const data = await response.json();

    const currentFile = productUrl.split('/').pop();
    const productName = currentFile.slice(0, -5).replace(/-/g, ' ');

    return getProductByName(data, productName);
  } catch (error) {
    console.error("Error al obtener y mostrar detalles:", error);
    return null;
  }
}

function getProductByName(products, productName) {
  for (const product of products) {
    if (product.nombre.toLowerCase() === productName.toLowerCase()) {
      return product;
    }
  }
  return null;
}
