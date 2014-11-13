//Bind pages to tabs
var pages = document.getElementById('pages');
var tabs = document.getElementById('tabs');
var aboutpages = document.getElementById('aboutpages');
var gamepages = document.getElementById('gamepages');

tabs.addEventListener('core-select', function() {
  // home page selected
  if(tabs.selected == 0){ 
    pages.selected = 0;
    gamepages.selected = -1;
    aboutpages.selected = -1;
  } // game page selected
  else if (tabs.selected == 1){
    pages.selected = -1;
    gamepages.selected = 0;
    aboutpages.selected = -1;
  } // about page selected
  else if (tabs.selected == 2){
    pages.selected = -1;
    gamepages.selected = -1;
    aboutpages.selected = 0;
  }

});