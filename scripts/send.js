
function mapClickListener(){
    $(document).ready(function(){
        $('.hex').click(function(){
            console.log("clicked");
            var row = this.getAttribute('row');
            var col = this.getAttribute('col');
            console.log(col, ', ', row);
            var coord = { 'row':row, 'column':col };
            $.ajax({ // send col and row
                url: '/map',
                type: 'POST',
                data: coord,
                dataType: 'json',
                success: function(data){
                    console.log("asdf");
                }
            });
            // show paper-dropdown for hex
            hexDropClickListener();
            return false;
        });
    });
}

function startListener(){
    $(document).ready(function(){
        $('.start').click(function(){
            var begin = {'start':"start"};
            $.ajax({
                url: '/start',
                type: 'POST',
                data: begin,
                dataType: 'json',
                success: function(data){
                    console.log("starting game");
                }
            });
            return false;
        });
    });
}

// creates a drop-down menu after the user clicks on a hex
function hexDropClickListener(){ 
    var menu, inner, i, numItems, menuItems;
    if ( {{unit}} ){
        menu = document.createElement('paper-dropdown');
        form = document.createElement('form');
        inner = document.createElement('div');
        form.id = "dropdown";
        form.action = "/action";
        numItems = {{n_items}};
        menuItems = {{menu_items}};
        for (i = 0; i < numItems; i=i+1){ // create multiple menu items to show
            var item = document.createElement('paper-item');
            menu.appendChild(item);
            item.className = 'item';
            item.innerHTML = menuItems[i];
        }
    }
    // when an item in the menu is clicked, we need to send that data to backend
    $(document).ready(function(){
        $('.item').click(function() { 
            var itemClicked = this.innerHTML;
            var data = {'item': itemClicked};
            $.ajax({
                url = '/action';
                type: 'POST',
                data: begin,
                dataType: 'json',
                success: function(data){
                    console.log("giving action");
                }
            });
            return false;
        });
    });
}
