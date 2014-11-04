//Bind pages to tabs
var pages = document.getElementById('pages');
var tabs = document.getElementById('tabs');
tabs.addEventListener('core-select', function() {
  pages.selected = tabs.selected;
});