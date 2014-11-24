//Bind pages to tabs
var pages = document.getElementById('pages');
var tabs = document.getElementById('tabs');
var aboutpages = document.getElementById('aboutpages');
var gamepages = document.getElementById('gamepages');
var gamehome = document.getElementById('gamehome');
<<<<<<< HEAD
var button = document.querySelector('.start');
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
    gamehome.style.display = "";
    aboutpages.style.display = "none";
    button.disabled = false;
  } // about page selected
  else if (tabs.selected == 2){
    pages.style.display = "none";
    gamepages.style.display = "none";
    aboutpages.selected = 0;
    aboutpages.style.display = "";
  }

});
=======
if (tabs.addEventListener){
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
	    gamehome.style.display = "";
	    aboutpages.style.display = "none";
	  } // about page selected
	  else if (tabs.selected == 2){
	    pages.style.display = "none";
	    gamepages.style.display = "none";
	    aboutpages.selected = 0;
	    aboutpages.style.display = "";
	  }
	});
} else if (tabs.attachEvent){
	tabs.attachEvent('core-select', function() {
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
	    gamehome.style.display = "";
	    aboutpages.style.display = "none";
	  } // about page selected
	  else if (tabs.selected == 2){
	    pages.style.display = "none";
	    gamepages.style.display = "none";
	    aboutpages.selected = 0;
	    aboutpages.style.display = "";
	  }
	});
}
>>>>>>> 8a0a1569a121044617af0ad8311e1774f1c479a2
