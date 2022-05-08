import { myGeoJSON } from "./gate-tile-map.js"

// CREATE IMAGE ELEMENT AND GET THE SOURCE
var image = document.createElement("img")
image.src = "./gate3.png"

// CREATE INITIAL MAP AND IMAGE OVERLAY
var map = L.map("map", {attributionControl: false}).setView([0, 0], 4)
// var imageOverlay = L.imageOverlay(image, [[-20, -30], [20, 30]]).addTo(map)
var imageOverlay = L.imageOverlay(image, [[-20, -40], [20, 40]]).addTo(map)

// STYLING INFORMATION FOR EACH POLYGON
var myStyle = {
    "color": "#ff7800",
    "weight": 2,
    "opacity": 0.5
}

// FUNCTION TO APPLY TO EACH FEATURE
function myOnEachFeature(feature, layer) {
    layer.on("mouseover", function(e) {
        layer.setStyle({
            "color": "red"
        })
    })
    layer.on("mouseout", function(e) {
        layer.setStyle({
            "color": "#ff7800"
        })
    })
    layer.bindPopup(feature.properties.name + "<br>" + feature.properties.text)
}

// COMBINE EVERYTHING TO LOAD IN GEOJSON FILE
L.geoJSON(myGeoJSON,
{
    style: myStyle,
    onEachFeature: myOnEachFeature
}).addTo(map)

// ON-CLICK COORDINATE TOOL FOR MAP
//    This is responsible for logging the lattitude and logitude of a point
//    into the console, and is useful for creating the geojson objects.
var coords = []
map.on("click", function(e) {
    coords.push([e.latlng.lng, e.latlng.lat])
})

// DETECT KEYBOARD INPUTS AND PERFORM LIST MANIPULATIONS ACCORDINGLY
document.addEventListener("keypress", function(e) {
    switch (e.key) {
        case "p":
            // detects if list is empty
            if (coords.length == 0) {
                console.log("list is empty")
                break
            }
            // prints the list to be put into geojson
            var rtnStr = ""
            for (let i = 0; i < coords.length - 1; i++) {
                rtnStr += "[" + coords[i][0] + ", " + coords[i][1] + "],\n"
            }
            rtnStr += "[" + coords[coords.length - 1][0] + ", " + coords[coords.length - 1][1] + "]"
            console.log(rtnStr)
            break
        case "c":
            // clears the list and allows for it to be used again
            coords = []
            break
        default:
            break
    }
})
