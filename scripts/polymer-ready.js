// Wait for 'polymer-ready'. Ensures the element is upgraded.
window.addEventListener('polymer-ready', function(e) {
  var ajax = document.querySelector('core-ajax');

  // Respond to events it fires.
  ajax.addEventListener('core-response', function(e) {
    console.log(this.response);
  });

  ajax.go(); // Call its API methods.
});