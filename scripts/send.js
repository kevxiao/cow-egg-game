
function mapClickListener(){
    $(document).ready(function(){
        $('.hex').click(function(){
            console.log("clicked");
            var row = this.getAttribute('row');
            var col = this.getAttribute('col');
            console.log(col, ', ', row);
            var coord = { 'row':row, 'column':col };
            $.ajax({
                url: '/',
                type: 'POST',
                data: coord,
                dataType: 'json',
                success: function(data){
                    console.log("asdf");
                }
            });
            return false;
        });
    });
}
