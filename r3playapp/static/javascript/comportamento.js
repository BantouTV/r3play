$(document).ready(function() {
    $('#filtro_genero').change(function(event){
        $(event.target).parent('form').submit();
    });
    
    $('#filtro_ano').change(function(event){
        $(event.target).parent('form').submit();
    });
    
    $('#filtro_nacionalidade').change(function(event){
        $(event.target).parent('form').submit();
    });
    
    $('#filtro_alfabeto').change(function(event){
        $(event.target).parent('form').submit();
    });

    $('#filtro_estados').change(function(event){
        $(event.target).parent('form').submit();
    });    
});