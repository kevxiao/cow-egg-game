// makes the map for the game
var map = document.getElementById("map"); 
// var row = document.createAttribute('row'); // row of the hexagon
// var col = document.createAttribute('col'); // column of the hexagon
function createmap() {
    // console.log("in createmap")
    var length = 5, i = 0, j = 0, rowEle, space, ripple;
    for (i = 0; i < length; i = i + 1) {
        rowEle = document.createElement('OL');
        map.appendChild(rowEle);
        if (i % 2 === 0) {
            rowEle.className = 'even';
        } else {
            rowEle.className = 'odd';
        }
        var row = document.createAttribute('row'); // row of the hexagon
        row.value = i;
        rowEle.setAttributeNode(row);
        for (j = 0; j < length; j = j + 1) {
            console.log("in j");
            space = document.createElement('LI');
            rowEle.appendChild(space);
            space.className = 'hex';
            var col = document.createAttribute('col'); // column of the hexagon
            col.value = j;
            space.setAttributeNode(col);
        }
    }
}
