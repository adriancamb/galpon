
const searchResultsGrid = document.getElementById('searchResultsGrid');
const paginationContainer = document.getElementById('pagination');

const storedFilteredResults = localStorage.getItem('filteredResults');

if (storedFilteredResults) {
    const filteredResults = JSON.parse(storedFilteredResults);
    const itemsPerPage = 8; // Cantidad de resultados por página
    let currentPage = 1;

    function displayResults(page) {
        searchResultsGrid.innerHTML = ''; // Limpiar resultados actuales

        const startIndex = (page - 1) * itemsPerPage;
        const endIndex = startIndex + itemsPerPage;

        for (let i = startIndex; i < endIndex && i < filteredResults.length; i++) {
            const item = filteredResults[i];
            const categoryName = item.url.split('/').slice(-2, -1)[0];
            const indiceUltimaBarra = item.url.lastIndexOf("/");
            const categoriaUrl = item.url.substring(0, indiceUltimaBarra) + ".html";

            const resultHtml = `
                <div class="search-result">
                    <div class="preview">
                        <img src="${item.imagen}" alt="${item.nombre}" class="preview-image">
                    </div>
                    <div class="result-details">
                        <h4><a href="${item.url}" class="product-link">${item.nombre}</a></h4>
                        <p>Precio: $${item.precio}</p>
                        <p class="product-category" style="text-align: right;">
                            <a href="${categoriaUrl}" class="category-link">${categoryName}</a>
                        </p>
                    </div>
                </div>
            `;
            searchResultsGrid.innerHTML += resultHtml;
        }
    }

    displayResults(currentPage);

    // Agregar el texto de información de resultados
    const searchTerm = localStorage.getItem('searchTerm');
    const resultCount = filteredResults.length;
    const searchInfo = document.getElementById('searchInfo');
    searchInfo.innerHTML = `Se encontraron ${resultCount} productos que coinciden con "${searchTerm}"`;

    // Crear enlaces de paginación
    const totalPages = Math.ceil(filteredResults.length / itemsPerPage);
    const paginationHtml = `
        <ul class="pagination">
            ${Array.from({ length: totalPages }, (_, i) => `
                <li class="page-item ${currentPage === i + 1 ? 'active' : ''}">
                    <a class="page-link" href="#" data-page="${i + 1}">${i + 1}</a>
                </li>
            `).join('')}
        </ul>
    `;

    paginationContainer.innerHTML = paginationHtml;

    // Manejar clic en enlaces de paginación
    paginationContainer.addEventListener('click', (event) => {
        event.preventDefault();
        if (event.target.tagName === 'A') {
            currentPage = parseInt(event.target.dataset.page);
            displayResults(currentPage);
        }
    });
}
