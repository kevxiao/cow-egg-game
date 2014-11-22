// makes the map for the game
var map = document.getElementById("map");
function createmap() {
    console.log("in createmap")
    var length = 5, i = 0, j = 0, row, space;
    for (i = 0; i < length; i = i + 1) {
        console.log("in i");
        console.log(i);
        row = document.createElement('OL');
        map.appendChild(row);
        if (i % 2 === 0) {
            row.className = 'even';
        } else {
            row.className = 'odd';
        }
        for (j = 0; j < length; j = j + 1) {
            console.log("in j");
            space = document.createElement('LI');
            row.appendChild(space);
            space.className = 'hex';
        }
    }
}
