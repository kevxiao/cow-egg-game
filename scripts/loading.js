
var button = document.querySelector('.start');
function startLoading(){

	// button.disabled = true;
	var progress = document.createElement('paper-progress');
	loop = document.createAttribute('indeterminate');
	progress.setAttributeNode(loop);
	// loop to wait until done loading
	// for (; ;){
	// 	if ( {{done_loading}} ){
	// 		return;
	// 	}
	// }
}
// https://www.polymer-project.org/components/paper-progress/demo.html