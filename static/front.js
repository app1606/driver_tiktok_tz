ymaps.ready(init);

function init () {
    var request = new XMLHttpRequest();
    request.open('GET', 'http://127.0.0.1:4351/get');
    request.send();
    var myMap = new ymaps.Map("map", {
        center: [54.83, 37.11],
        zoom: 5
    }, {
        searchControlProvider: 'yandex#search'
    });
    request.onload = function () { //adds all landmarks
        data = JSON.parse(request.response);
        for ( var key in data.detail){
            console.log(data.detail[key].latitude);
            myPlacemark = new ymaps.Placemark([data.detail[key].latitude, data.detail[key].longitude], {
                balloonContentHeader: `Балун ${key}ой метки`,
                balloonContentBody: `Latitude: ${data.detail[key].latitude}, Longitude: ${data.detail[key].longitude}`,
                balloonContentFooter: `Это ${key }ая метка`,
                hintContent: `Метка ${key}`
            });  
            myMap.geoObjects.add(myPlacemark);  
        }
    };
    myMap.events.add('click', function (e) { //shows coordinates of the place that user clicked on 
        if (!myMap.balloon.isOpen()) {
            var coords = e.get('coords');
            myMap.balloon.open(coords, {
                contentHeader:'',
                contentBody:'<p>Если хотите добавить метку, введите данные в форму выше.</p>' +
                    '<p>Координаты щелчка: ' + [
                    coords[0].toPrecision(6),
                    coords[1].toPrecision(6)
                    ].join(', ') + '</p>',
                contentFooter:''
            });
        }
        else {
            myMap.balloon.close();
        }
    });
    
}
function add() { //landmark addition
    var request = new XMLHttpRequest();
    var lat = document.getElementById("lat").value;
    var long = document.getElementById("long").value;
    request.open('GET', `http://127.0.0.1:4351/add?lat=${lat}&long=${long}`);
    request.send();
    window.location.reload(true);

}

function del() { //landmark deletion
    var request = new XMLHttpRequest();
    var lat = document.getElementById("lat").value;
    var long = document.getElementById("long").value;
    request.open('GET', `http://127.0.0.1:4351/delete?lat=${lat}&long=${long}`);
    request.send();
    window.location.reload(true);
}