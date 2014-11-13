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

