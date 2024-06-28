function agregarProductosCarrito(nombre, precio)
{
    const producto = {nombre, precio, cantidad:1};
    let carrito = JSON.parse(localStorage.getItem("carrito")) || [];
   
    const index = carrito.findIndex(p => p.nombre === nombre);
    if(index !== -1){
        carrito[index].cantidad +=1;
    }else{
        carrito.push(producto);
    }
    
    localStorage.setItem("carrito", JSON.stringify(carrito));
    actualizarTotal();
}
   
function eliminarProductosCarrito(index)
{
    let carrito = JSON.parse(localStorage.getItem("carrito")) || [];
    carrito.splice(index, 1);
    localStorage.setItem("carrito", JSON.stringify(carrito));
    cargarCarrito();
    actualizarTotal();
}

function cargarCarrito()
{
    let carrito = JSON.parse(localStorage.getItem("carrito")) || [];
    const tbody = document.getElementById("cart-items");
    tbody.innerHTML = "";

    carrito.forEach((producto, index)=>
    {
        const newRow = document.createElement("tr");

        const nameCell = document.createElement("td");
        nameCell.textContent = producto.nombre;
        newRow.appendChild(nameCell);

        const priceCell = document.createElement("td");
        priceCell.textContent = "$" + producto.precio;
        newRow.appendChild(priceCell);

        
        const quantityCell = document.createElement("td");
        quantityCell.textContent = producto.cantidad;
        newRow.appendChild(quantityCell);

        const totalPriceCell = document.createElement("td");
        totalPriceCell.textContent = "$" + (producto.precio * producto.cantidad);
        newRow.appendChild(totalPriceCell);

        const deleteCell = document.createElement("td");
        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Eliminar";
        deleteButton.classList.add("btn, btn-danger");
        deleteButton.onclick = () => eliminarProductosCarrito(index);
        deleteCell.appendChild(deleteButton);
        newRow.appendChild(deleteCell);

    }); 

    actualizarTotal();
}

function actualizarTotal()
{
    let carrito = JSON.parse(localStorage.getItem("carrito")) || [];
    const totalPriceElement = document.getElementById("total-price");
    const totalPrice = carrito.reduce((total, producto) => total + (producto.precio * producto.cantidad), 0);
    totalPriceElement.textContent = "$" + totalPrice;
}

document.addEventListener("DOMContentLoaded", cargarCarrito);