// Switching pages on About page
var tabs = document.getElementById('tabs');
document.querySelector('.change').onclick = function(e) {
    if (tabs.selected == 2) {
        this.selected = (this.selected + 1) % this.items.length;
        this.async(function() {
            if (this.selectedIndex == 0) {
                this.selectedItem.classList.remove('begin');
            } else if (this.selectedIndex == this.items.length - 1) {
                this.items[0].classList.add('begin');
            }
        });
    }
};
// Switch pages on game page
var gamepages = document.getElementById('gamepages');
var gamehome = document.getElementById('gamehome');
var mapFlag = 1;
document.querySelector('.start').onclick = function(e) {
    if (tabs.selected == 1) {
        gamepages.selected = 1; // show the ingame page
        if (mapFlag){ // make map only once
            createmap();
            startLoading();
            gamehome.style.display = "none"; // change depending on the current page
            // when done loading, display map
            var map = document.getElementById("map"); 
            // map.style.display = "";
            mapClickListener();
            mapFlag = 0;
        }
    }
};


