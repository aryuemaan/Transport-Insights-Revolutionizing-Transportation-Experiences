fetch('/api/ride_data')
    .then(response => response.json())
    .then(data => {
        // Manipulate and display the ride data on the webpage
    });

fetch('/api/transportation_data')
    .then(response => response.json())
    .then(data => {
        // Manipulate and display the transportation data on the webpage
    });

fetch('/api/delivery_data')
    .then(response => response.json())
    .then(data => {
        // Manipulate and display the delivery data on the webpage
    });
