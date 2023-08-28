$(document).ready(function() {
    const searchInput = $('#searchInput');
    const searchResults = $('#searchResults');
    const searchButton = $('#searchButton');
    let jsonData;
    
    // Cargar los datos desde el archivo JSON
    $.getJSON('/productos/productos.json', function(Data) {
        jsonData = Data; // Asignar los datos cargados a la variable jsonData
        
        searchInput.on('input', function() {
            const searchTerm = $(this).val().toLowerCase();
    
            if (searchTerm.length === 0) {
                searchResults.empty();
                return;
            }
    
            const filteredResults = jsonData.filter(item => {
                return item.nombre.toLowerCase().includes(searchTerm);
            });
    
            searchResults.empty();
    
            if (filteredResults.length === 0) {
                searchResults.append('<p>No se encontraron resultados.</p>');
            } else {
                filteredResults.forEach(item => {
                    // Extraer la categoría de la URL del producto
                    const categoryName = item.url.split('/').slice(-2, -1)[0];
                    const indiceUltimaBarra = item.url.lastIndexOf("/");
                    //esta es la ruta de la categoria que se obtiene desde el producto
                    const categoriaUrl = item.url.substring(0, indiceUltimaBarra) + ".html";
    
                    const resultHtml = `
                        <div class="search-result">
                            <div class="preview">
                                <img src="${item.imagen}" alt="${item.nombre}" class="preview-image">
                            </div>
                            <div class="result-details">
                                <h4><a href="${item.url}" class="product-link">${item.nombre}</a></h4>
                                <p class="product-category"style="text-align: right;"> <a href="${categoriaUrl}" class="category-link">Ver todo en ${categoryName}</a></p>
                            </div>
                        </div>
                    `;
                    searchResults.append(resultHtml);
                });
            }
        });
    });

    searchButton.click(function() {
        if (!jsonData) {
            console.error("Error: jsonData not loaded yet.");
            return;
        }
        const searchTerm = searchInput.val().toLowerCase();
        const filteredResults = jsonData.filter(item => {
            return item.nombre.toLowerCase().includes(searchTerm);
        });
    
        // Redirigir a la página de resultados con la cantidad de resultados y el término de búsqueda
        redirectToBusquedaPage(filteredResults, searchTerm);
    });
    
    function redirectToBusquedaPage(filteredResults, searchTerm) {
        localStorage.setItem('filteredResults', JSON.stringify(filteredResults));
        localStorage.setItem('searchTerm', searchTerm);
        window.location.href = '/productos/busqueda.html';
    }
});