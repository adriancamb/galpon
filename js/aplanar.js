const fs = require('fs');

function flattenCategories(categories) {
    const flattenedProducts = [];

    function flattenProducts(products, parentName = "") {
        for (const product of products) {
            const newProduct = {
                ...product,
                parent: parentName
            };

            flattenedProducts.push(newProduct);

            if (product.subproductos) {
                flattenProducts(product.subproductos, product.nombre);
                delete newProduct.subproductos;
            }
        }
    }

    for (const category of categories) {
        flattenProducts(category.productos);
    }

    return flattenedProducts;
}

fs.readFile('../productos/categorias.json', 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading the file:', err);
        return;
    }

    try {
        const originalData = JSON.parse(data);
        const flattenedData = flattenCategories(originalData.categorias);
        console.log(JSON.stringify(flattenedData, null, 2));
    } catch (parseError) {
        console.error('Error parsing JSON:', parseError);
    }
});
