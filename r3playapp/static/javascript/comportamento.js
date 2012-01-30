$(document).ready(function() {
    $('#filtro_genero').change(function(event){
        $(event.target).parent().submit();
    });
    
    $('#filtro_ano').change(function(event){
        $(event.target).parent().submit();
    });
    
    $('#filtro_nacionalidade').change(function(event){
        $(event.target).parent().submit();
    });
    
    $('#filtro_alfabeto').change(function(event){
        $(event.target).parent().submit();
    });
});