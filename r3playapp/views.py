from r3play.r3playapp.models import Filmes
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    return render_to_response('index.html')
    
def home(request):
    lista_ultimos_filmes = Filmes.objects.all()[:15]
    return render_to_response('home.html', {'lista_ultimos_filmes': lista_ultimos_filmes}, context_instance=RequestContext(request))
    

def filme(request, filme_id):
    filme = get_object_or_404(Filmes, id=filme_id)
    return render_to_response('filme.html', {'filme': filme})
    
