from r3play.r3playapp.models import Filmes
from r3play.r3playapp.models import Artistas
from r3play.r3playapp.utils import Util
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse

def index(request):
    return render_to_response('index.html')
    
def home(request):
    lista_ultimos_filmes = Filmes.objects.all()[:15]
    util = Util()
    frase = util.frase_randomica()
    return render_to_response('home.html', {'lista_ultimos_filmes': lista_ultimos_filmes, 'frase': frase}, context_instance=RequestContext(request))
    
def filme(request, filme_id):
    filme = get_object_or_404(Filmes, id=filme_id)
    return render_to_response('filme.html', {'filme': filme}, context_instance=RequestContext(request))
    
def busca(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(titulo_nacional__icontains=query) |
            Q(titulo_original__icontains=query) 
        )
        resultados = Filmes.objects.filter(qset).distinct()
    else:
        resultados = []
    return render_to_response("resultado_busca.html", {
        "resultados": resultados,
        "query": query
    }, context_instance=RequestContext(request))
    
def categorias(request):
    return HttpResponse("Categorias!")
    
def artistas(request):
    lista_artistas = Artistas.objects.all()[:15]
    return render_to_response('artistas.html', {'lista_artistas': lista_artistas}, context_instance=RequestContext(request))
    
def artista(request, artista_id):
    artista = get_object_or_404(Artistas, id=artista_id)
    return render_to_response('artista.html', {'artista': artista}, context_instance=RequestContext(request))
    
def usuarios(request):
    return HttpResponse("Usuarios!")
    
def cinemas(request):
    return HttpResponse("Cinemas")
    
#def p404(request):
#    return render_to_response('404.html', context_instance=RequestContext(request))