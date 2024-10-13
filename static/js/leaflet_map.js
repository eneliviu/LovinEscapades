/**
 * Initializes a Leaflet map displaying trip locations with clustering.
 
 * Functionality:
 * - Creates map centered on Greenwich with zoom and scale controls.
 * - Loads location data from JSON, creating markers with popups 
 *      containing trip details.
 * - Clusters the markers for better visualization.
 * - Adjusts the map view dynamically to fit markers.
 * - Moves to a marker's location on click.
 */
document.addEventListener('DOMContentLoaded', function () {
    // Default coordinates for Greenwich
    var map = L.map('map', { zoomControl: true }).setView([51.4934, 0.0098], 3);

    // Adding scale control
    var scale = L.control.scale();
    scale.addTo(map);

    L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 19,
        attribution: "&copy;" +
                     '<a href="http://www.openstreetmap.org/copyright">' +
                     "OpenStreetMap</a>"
    }).addTo(map);

    // Parse the JSON data from the script tag
    var locations = JSON.parse(document.getElementById("trips_json")
        .textContent);
    if (!Array.isArray(locations)) {
        locations = [locations];
    }

    var markers = L.markerClusterGroup();
    if (Object.keys(locations)) {
        locations.forEach(element => {
            // Determine the URL based on authentication status
            // console.log(isAuthenticated)
            // let moreUrl = isAuthenticated ? '/gallery/' : '/accounts/signup/';
            let marker = L.marker([element.lat, element.lon])
                .bindPopup(
                    "<div>" +
                        "<b>" + element.place + ", " + element.country + "</b>" +
                        "</br>" +
                        "<b>" + element.trip_category + "</b>" +
                        "</br>" +
                        "From: " + element.start_date + "</br>" +
                        "To: " + element.end_date +
                        "</br>" +
                        '<div class="text-center" >' + 
                            "<a href='/gallery/' class='badge text-bg-primary' rel='noopener noreferrer'>" + 
                                '<span class="fs-6 text-center">' + "More..." + '</span>' + 
                            "</a>" +
                        "</div>"
                            +
                    "</div>"
                );
            markers.addLayer(marker);
        });

        map.addLayer(markers);

        if (Object.keys(locations).length > 1) {
            var bounds = markers.getBounds();
            if (bounds.isValid()) {
                map.fitBounds(bounds, { maxZoom: 8 });
            }
        }

        markers.on("click", function (e) {
            map.flyTo(e.latlng, 6);
        });
    }
});