//Bind pages to tabs
var pages = document.getElementById('pages');
var tabs = document.getElementById('tabs');
var aboutpages = document.getElementById('aboutpages');
tabs.addEventListener('core-select', function() {
  pages.selected = tabs.selected;
  if(pages.selected != 2) {
  		aboutpages.selected=-1
  }else{
  		aboutpages.selected=0
  }
});