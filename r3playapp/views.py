from r3play.r3playapp.models import Filmes
from r3play.r3playapp.models import Artistas
from r3play.r3playapp.models import Generos
from r3play.r3playapp.utils import Util
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse

util                            = Util()

def index(request):
    return render_to_response('index.html')
    
def home(request):
    frase                       = util.frase_randomica()
    lista_generos               = Generos.objects.all().order_by('nome')
    filtro_genero               = request.GET.get('genero', '')
    filtro_ano                  = request.GET.get('ano', '')
    filtro_tipo                 = request.GET.get('tipo', '')
    
    # filtrando os resultados
    if filtro_genero:
        lista_ultimos_filmes            = Filmes.objects.all().filter(genero__id__exact = filtro_genero)[:15]
    elif filtro_ano:
        lista_ultimos_filmes            = Filmes.objects.all().filter(ano_lancamento__exact = filtro_ano)[:15]
    elif filtro_tipo:
        if filtro_tipo == 'todos':
            lista_ultimos_filmes        = Filmes.objects.all()[:15]
        else :
            lista_ultimos_filmes        = Filmes.objects.all().filter(tipo__contains = filtro_tipo)[:15]
    else:
        lista_ultimos_filmes            = Filmes.objects.all()[:15]
    
    return render_to_response('home.html', {
                                        'lista_ultimos_filmes':         lista_ultimos_filmes, 
                                        'frase':                        frase,
                                        'lista_generos':                lista_generos,
                                        'anos':                         range(2000,2013),
                                        'tipo':                         filtro_tipo
                                        }, context_instance=RequestContext(request))
    
def filme(request, filme_id):
    filme                       = get_object_or_404(Filmes, id=filme_id)
    frase                       = util.frase_randomica()
    
    return render_to_response('filme.html', {
                                        'filme': filme, 
                                        'frase': frase
                                        }, context_instance=RequestContext(request))
    
def busca(request):
    query                       = request.GET.get('q', '')
    frase                       = util.frase_randomica()
    
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
                                                    "query": query,
                                                    'frase': frase
                                                    }, context_instance=RequestContext(request))
    
def categorias(request):
    return HttpResponse("Categorias!")
    
def artistas(request):
    lista_artistas              = Artistas.objects.all().order_by('nome')[:15]
    frase                       = util.frase_randomica()
    
    return render_to_response('artistas.html', {
                                            'lista_artistas': lista_artistas, 
                                            'frase': frase
                                            }, context_instance=RequestContext(request))
    
def artista(request, artista_id):
    artista                     = get_object_or_404(Artistas, id=artista_id)
    filmes                      = Filmes.objects.filter(
                                                            artistas__contains = artista.nome
                                                        ).order_by(
                                                            'ano_lancamento'
                                                        ).reverse()
    ultimo_filme                = filmes[0] if filmes else None #retorna None se filmes estiver vazio
    frase                       = util.frase_randomica()
    
    return render_to_response('artista.html', {
                                            'artista': artista, 
                                            'filmes': filmes, 
                                            'ultimo_filme': ultimo_filme, 
                                            'frase': frase
                                            }, context_instance=RequestContext(request))
    
def usuarios(request):
    return HttpResponse("Usuarios!")
    
def cinemas(request):
    return HttpResponse("Cinemas")