$(document).ready(function(){
    $('#productForm').validate({
        rules: {
            productName: {
                required: true,
                minlength: 3
            },
            productPrice: {
                required: true,
                number: true,
                min: 1,
            }
        },
        messages: {
            productName: {
                required: "Por favor, introduce el nombre del producto",
                minlength: "El nombre del producto debe tener al menos 3 caracteres"
            },
            productPrice: {
                required: "Por favor, introduce el precio del producto",
                number: "El precio del producto debe ser un número",
                min: "El precio del producto debe ser mayor que 0"
            }
        },
        submitHandler: function(form) {
            addProduct();
            form.reset();
            return false;
        }
    });
    loadProducts();
});

function addProduct(){
    var ProductName = $('#productName').val();
    var ProductPrice = $('#productPrice').val();
    var product = { ProductName, ProductPrice }

    appendProductToTable(ProductName, ProductPrice);
    saveProductoToStorage(product);
}

function editProduct(button){
    var row = $(button).closest('tr');
    var cols = row.children('td');
    if(button.textContent == 'Editar'){
        $(cols[0]).html(`<input type="text" class="form-control" value="${$(cols[0]).text()}">`);
        $(cols[1]).html(`<input type="number" class="form-control" value="${$(cols[1]).text()}">`);
        $(button).text('Guardar').removeClass('btn-info').addClass('btn-success');
        $(button).next().text('Cancelar').removeClass('btn-danger').addClass('btn-warning');
    } else { // Guardar
        var newName = $(cols[0]).find('input').val();
        var newPrice = $(cols[1]).find('input').val();
        $(cols[0]).text(newName);
        $(cols[1]).text(newPrice);
        $(button).text('Editar').removeClass('btn-success').addClass('btn-info');
        $(button).next().text('Eliminar').removeClass('btn-warning').addClass('btn-danger');
        updateProductInStorage(row.index(), newName, newPrice);
    }
}

function updateProductInStorage(index, newName, newPrice){
    var products = JSON.parse(localStorage.getItem('products'));
    products[index].ProductName = newName;
    products[index].ProductPrice = newPrice;    
    localStorage.setItem('products', JSON.stringify(products));
}

function deleteProduct(button){
    var row = $(button).closest('tr');
    var cols = row.children('td');
    if(button.textContent === 'Cancelar'){
        $(cols[0]).text($cols[0]).find('input').val();
        $(cols[1]).text($cols[1]).find('input').val();
        $(button).prev().text('Editar').removeClass('btn-warning').addClass('btn-info');
        $(button).text('Eliminar').removeClass('btn-warning').addClass('btn-danger');
    } else {
        removeFormStorage(row.index());
        row.remove();
    }
}

function removeFormStorage(index){
    var products = JSON.parse(localStorage.getItem('products'));
    products.splice(index, 1);
    localStorage.setItem('products', JSON.stringify(products));
}

function loadProducts() {
    if(localStorage.getItem('products')){
        var products = JSON.parse(localStorage.getItem('products'));
        products.forEach(function(product){
            appendProductToTable(product.ProductName, product.ProductPrice);
        });
    }
}

function appendProductToTable(name, price) {
    $('#productsTable tbody').append(`
        <tr>
            <td>${name}</td>
            <td>${price}</td>
            <td>
                <button class="btn btn-info" onclick="editProduct(this)">Editar</button>
                <button class="btn btn-danger" onclick="deleteProduct(this)">Eliminar</button>
            </td>
        </tr>
    `);
}

function saveProductoToStorage(product){
    var products = localStorage.getItem('products') ? JSON.parse(localStorage.getItem('products')) : [];
    // If lineal ? => If true : If false
    products.push(product);
    localStorage.setItem('products', JSON.stringify(products));
}