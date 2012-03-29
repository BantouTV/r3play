#!/usr/bin/env python
# encoding: utf-8

from r3play.r3playapp.models import Filmes
from r3play.r3playapp.models import Artistas
from r3play.r3playapp.models import Diretores
from r3play.r3playapp.models import Generos
from r3play.r3playapp.models import Cinemas
from r3play.r3playapp.utils import Util
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from django.core.paginator import Paginator

util                            = Util()
lista_generos                   = Generos.objects.all().order_by('nome')
alfabeto                        = util.lista_alfabeto()
anos                            = range(2000,2013)

def index(request):
    return render_to_response('index.html')

def home(request):
    frase                       = util.frase_randomica()
    filtro_genero               = request.GET.get('genero', '')
    filtro_ano                  = request.GET.get('ano', '')
    filtro_tipo                 = request.GET.get('tipo', '')
    
    # filtrando os resultados
    if filtro_genero:
        if filtro_genero == 'todos':
            lista_ultimos_filmes            = Filmes.objects.all()[:15]
        else:
            lista_ultimos_filmes            = Filmes.objects.all().filter(genero__id__exact = filtro_genero)[:15]
    elif filtro_ano:
        if filtro_ano == 'todos':
            lista_ultimos_filmes            = Filmes.objects.all()[:15]
        else:
            lista_ultimos_filmes            = Filmes.objects.all().filter(ano_lancamento__exact = filtro_ano)[:15]
    elif filtro_tipo:
        if filtro_tipo == 'todos':
            lista_ultimos_filmes            = Filmes.objects.all()[:15]
        else :
            lista_ultimos_filmes            = Filmes.objects.all().filter(tipo__contains = filtro_tipo)[:15]
    else:
        lista_ultimos_filmes                = Filmes.objects.all()[:15]


    return render_to_response('home.html', {
                                        'lista_ultimos_filmes':         lista_ultimos_filmes, 
                                        'frase':                        frase,
                                        'lista_generos':                lista_generos,
                                        'anos':                         anos,
                                        'tipo':                         filtro_tipo
                                        }, context_instance=RequestContext(request))
                                        

def filme(request, filme_id):
    filme                       = get_object_or_404(Filmes, id=filme_id)
    frase                       = util.frase_randomica()
    lista                       = filme.artistas.split(',')
    lista_diretores_string      = filme.diretores.split(',')
    lista_artistas              = []
    lista_diretores             = []
    
    for nome_artista in lista:
        nome_artista                = nome_artista.strip()
        artista_atual               = Artistas.objects.filter( nome__exact = nome_artista )
        pk_lista                    = artista_atual.values('pk')
        artista                     = 0
        url                         = '/artista/'
        
        for pk in pk_lista:
            artista                 = pk['pk']
    
        lista_artistas.append( {'nome' : nome_artista, 'url' : url + str(int(artista))} )
    
    for nome_diretor in lista_diretores_string:
        nome_diretor                = nome_diretor.strip()
        diretor_atual               = Diretores.objects.filter( nome__exact = nome_diretor )
        pk_lista                    = diretor_atual.values('pk')
        diretor                     = 0
        url                         = '/diretor/'
        
        for pk in pk_lista:
            diretor                 = pk['pk']
    
        lista_diretores.append( {'nome' : nome_diretor, 'url' : url + str(int(diretor))} )


    return render_to_response('filme.html', {
                                        'filme':            filme, 
                                        'frase':            frase,
                                        'lista_artistas':   lista_artistas,
                                        'lista_diretores':  lista_diretores
                                        }, context_instance=RequestContext(request))

 
def busca(request):
    frase                       = util.frase_randomica()
    query                       = request.GET.get('q', '')
    filtro_genero               = request.GET.get('genero', '')
    filtro_ano                  = request.GET.get('ano', '')
    resultados_lista            = []
    page                        = request.GET.get('page')
    
    if query:
        qset = (
            Q(titulo_nacional__icontains=query) |
            Q(titulo_original__icontains=query) 
        )
        
        if filtro_genero:
            if filtro_genero == 'todos':
                resultados_lista                      = Filmes.objects.filter(qset).distinct()
            else:
                resultados_lista                      = Filmes.objects.filter(qset).distinct().filter(genero__id__exact = filtro_genero)
        
        elif filtro_ano:
            if filtro_ano == 'todos':
                resultados_lista                      = Filmes.objects.filter(qset).distinct()
            else:
                resultados_lista                      = Filmes.objects.filter(qset).distinct().filter(ano_lancamento__exact = filtro_ano)
        
        else:
            resultados_lista = Filmes.objects.filter(qset).distinct()
        
    else:
        resultados_lista = []
        
    # paginando os resultados
    paginator                       = Paginator(resultados_lista, 16) # mostra XX registros por pagina
    try:
        resultados                  = paginator.page( page )
    except:
        resultados                  = paginator.page( 1 )

    return render_to_response("resultado_busca.html", {
                                                    "resultados":       resultados,
                                                    "query":            query,
                                                    'frase':            frase,
                                                    'anos':             anos,
                                                    'lista_generos':    lista_generos
                                                    }, context_instance=RequestContext(request))
    
def categorias(request):
    return HttpResponse("Categorias!")
    
def artistas(request):
    lista_artistas              = Artistas.objects.all()
    lista_diretores             = Diretores.objects.all()

    frase                       = util.frase_randomica()
    filtro_nacionalidade        = request.GET.get('nacionalidade', '')
    filtro_nome                 = request.GET.get('nome', '')
    lista_artistas_por_pais     = lista_artistas.order_by('pais').distinct('pais')
    lista_paises                = []
    anterior                    = ''
    nacionalidade               = request.GET.get('nacionalidade')
    nome                        = request.GET.get('nome')
    page                        = request.GET.get('page')
    

    for item in lista_artistas_por_pais: # separando apenas os nomes de paises unicos
        item.pais = item.pais.lower().strip()
        if item.pais != anterior:
            lista_paises.append(item.pais)
            anterior = item.pais
        
    
    if filtro_nacionalidade:
        if filtro_nacionalidade != 'todos':
            lista_artistas          = lista_artistas.filter( pais__icontains = filtro_nacionalidade )
    else:
        nacionalidade               = ''
    
    if filtro_nome:
        if filtro_nome != 'todos':
            lista_artistas          = lista_artistas.filter( nome__istartswith = filtro_nome )
    else:
        nome                        = ''

    # paginando os resultados
    paginator                   = Paginator(lista_artistas, 16) # mostra XX registros por pagina
    try:
        artistas                = paginator.page( page )
    except:
        artistas                = paginator.page( 1 )
    
    
    return render_to_response('artistas.html', {
                                            'lista_artistas':   artistas, 
                                            'frase':            frase,
                                            'paises':           lista_paises,
                                            'alfabeto':         alfabeto,
                                            'nome':             nome,
                                            'nacionalidade':    nacionalidade
                                            }, context_instance=RequestContext(request))
    
def artista(request, artista_id):
    artista                     = get_object_or_404(Artistas, id=artista_id)
    filmes                      = Filmes.objects.filter( artistas__contains = artista.nome.strip()
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

                                          
def diretores(request):
    lista_diretores             = Diretores.objects.all()
    frase                       = util.frase_randomica()
    filtro_nacionalidade        = request.GET.get('nacionalidade', '')
    filtro_nome                 = request.GET.get('nome', '')
    lista_diretores_por_pais    = lista_diretores.order_by('pais').distinct('pais')
    lista_paises                = []
    anterior                    = ''
    nacionalidade               = request.GET.get('nacionalidade')
    nome                        = request.GET.get('nome')
    page                        = request.GET.get('page')
    
    
    for item in lista_diretores_por_pais: # separando apenas os nosmes de paises unicos
        item.pais = item.pais.lower().strip()
        if item.pais != anterior:
            lista_paises.append(item.pais)
            anterior = item.pais
    
    
    if filtro_nacionalidade:
        if filtro_nacionalidade != 'todos':
            lista_diretores          = lista_diretores.filter( pais__icontains = filtro_nacionalidade )
    else:
        nacionalidade               = ''
        
    if filtro_nome:
        if filtro_nome != 'todos':
            lista_diretores          = lista_diretores.filter( nome__istartswith = filtro_nome )
    else:
        nome                        = ''
        
    # paginando os resultados
    paginator                    = Paginator(lista_diretores, 16) # mostra XX registros por pagina
    try:
        diretores                = paginator.page( page )
    except:
        diretores                = paginator.page( 1 )
    
    

    return render_to_response('diretores.html', {
                                            'lista_diretores':      diretores, 
                                            'frase':                frase,
                                            'paises':               lista_paises,
                                            'alfabeto':             alfabeto,
                                            'nome':                 nome,
                                            'nacionalidade':        nacionalidade
                                            }, context_instance=RequestContext(request))

def diretor(request, diretor_id):
    diretor                     = get_object_or_404(Diretores, id=diretor_id)
    filmes                      = Filmes.objects.filter(
                                                            diretores__contains = diretor.nome.strip()
                                                        ).order_by(
                                                            'ano_lancamento'
                                                        ).reverse()
    ultimo_filme                = filmes[0] if filmes else None #retorna None se filmes estiver vazio
    frase                       = util.frase_randomica()            

    return render_to_response('diretor.html', {
                                            'diretor':          diretor, 
                                            'filmes':           filmes, 
                                            'ultimo_filme':     ultimo_filme, 
                                            'frase':            frase
                                            }, context_instance=RequestContext(request))
    
def usuarios(request):
    return HttpResponse("Usuarios!")
    
def cinemas(request):
    lista_cinemas               = Cinemas.objects.all()
    frase                       = util.frase_randomica()
    page                        = request.GET.get('page')
    lista_cinemas_por_estado    = lista_cinemas.order_by('estado').distinct('estado')
    lista_estados               = []
    anterior                    = ''
    filtro_nome                 = request.GET.get('nome')
    filtro_estado              = request.GET.get('estado')

    # separando apenas os nosmes de estados unicos
    for item in lista_cinemas_por_estado: 
        item.estado = item.estado.lower().strip()
        if item.estado != anterior:
            lista_estados.append(item.estado)
            anterior = item.estado

    if filtro_nome:
        if filtro_nome != 'todos':
            lista_cinemas           = lista_cinemas.filter( nome__istartswith = filtro_nome )
    else:
        nome                        = ''

    if filtro_estado:
        if filtro_estado != 'todos':
            lista_cinemas           = lista_cinemas.filter( estado__icontains = filtro_estado )
    else:
        nome                        = ''

    # paginando os resultados
    # mostra XX registros por pagina
    paginator                   = Paginator(lista_cinemas, 16) 
    try:
        cinemas                 = paginator.page( page )
    except:
        cinemas                 = paginator.page( 1 )


    return render_to_response('cinemas.html', {
                                            'lista_cinemas':    cinemas,
                                            'frase':            frase,
                                            'alfabeto':         alfabeto,
                                            'estados':          lista_estados
                                            }, context_instance=RequestContext(request))

def cinema(request, cinema_id):
    cinema                      = get_object_or_404(Cinemas, id=cinema_id)
    frase                       = util.frase_randomica()

    return render_to_response('cinema.html', {
                                            'cinema':           cinema,
                                            'frase':            frase
                                            }, context_instance=RequestContext(request))