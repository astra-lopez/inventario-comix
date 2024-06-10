// Hay mejores maneras de hacer esto -- ¡Qué pena!
/// N1: Offset nos dice desde que elemento empezamos a seleccionar.
///  Tiene que ser incrementado con cada llamado a la API para que no nos retorne 
///  entradas repetidas.
var offset = 0;
const limit = 100;
const filters = "field:id,field:volume,field:name,field:issue_number,field:cover_date,field:description";

const doRequest = () => {
    $.ajax({
        method: "GET",
        dataType: "jsonp",
        responseType: "application/json",
        crossDomain: true, 
        // Riesgo de seguridad, no guardar llaves de APIs en repos públicos -- ¡Qué pena!
        url: `https://comicvine.gamespot.com/api/issues/?api_key=c0a4c519ab6fd6ad7654ae0f1a732ebe7fc7811e&format=jsonp&offset=${offset}&limit=${limit}&filter=${filters}`,
        cache: true,
    }).then((data) => {
        oldData = JSON.parse(localStorage.getItem('data'));
        newData = oldData + data.results; 
        localStorage.setItem('data', JSON.stringify(newData));
        console.log(`Request exitosa de items ${offset} - ${offset + limit}.`);
        offset += limit; // @N1
    }).fail((_, status) => {
        alert(`Request falló: ${status}`); // ¡Felicidades, la API te botó!
    })
}

/// Actualiza 'stock-data' si y solo si hay datos en LS.
const renderStock = () => {
    $("#stock-data").html("");
    const data = JSON.parse(localStorage.getItem("data"));

    if (data) { 
        $.each(data, (_, val) => {
            $("#stock-data").append(
                '<tr>' + 
                '<td>' + val.id + '</td>' +
                '<td>' + val.volume.name + '</td>' +
                '<td>' + val.name + '</td>' +
                '<td>' + val.issue_number + '</td>' +
                '<td>' + val.cover_date + '</td>' + 
                '<td> </td>' +
                '</tr>'
            )
        })
     } 
}

/// Recarga el stock. Si 'request' es true entonces hace otro request.
///  Esto es para evitar hacer requests si ya hay valores en LS y no estamos
///  haciendo scroll al fondo de la página.
const reloadStock = (request) => { if (request) doRequest(); renderStock(); }

// Ejecutar función despues de cargar el DOM
$(() => { 
    // Quizás '===' sería más correcto -- ¡Qué pena!
    reloadStock(JSON.parse(localStorage.getItem("data")) == null);
});

// Recargar el stock al llegar al final
$(window).on('scroll', () => {
    reloadStock($(window).scrollTop() + $(window).height() > $(document).height - 100);
});

// ¡El código no se ve (tan) horrible! :')