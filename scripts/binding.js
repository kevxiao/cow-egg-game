//Bind pages to tabs
var pages = document.getElementById('pages');
var tabs = document.getElementById('tabs');
var aboutpages = document.getElementById('aboutpages');
var gamepages = document.getElementById('gamepages');

tabs.addEventListener('core-select', function() {
  // home page selected
  if(tabs.selected == 0){ 
    pages.selected = 0;
    pages.style.display = "";
    gamepages.style.display = "none";
    aboutpages.style.display = "none";
  } // game page selected
  else if (tabs.selected == 1){
    pages.style.display = "none";
    gamepages.selected = 0;
    gamepages.style.display = "";
    aboutpages.style.display = "none";
  } // about page selected
  else if (tabs.selected == 2){
    pages.style.display = "none";
    gamepages.style.display = "none";
    aboutpages.selected = 0;
    aboutpages.style.display = "";
  }

});