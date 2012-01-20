$(document).ready(function() {
    $('#filtro_genero').change(function(event){
        $(event.target).parent().submit();
    });
    
    $('#filtro_ano').change(function(event){
        $(event.target).parent().submit();
    });
});