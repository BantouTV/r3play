#!/usr/bin/env python
# encoding: utf-8

from r3play.r3playapp.models import Filmes
from random import choice

class Util:
    def __init__(self):
        pass
        
    def frase_randomica(self):
        lista_ultimos_filmes    = Filmes.objects.all()[:15]
        filme_randomico         = choice(lista_ultimos_filmes)
        
        if filme_randomico.frases == '':
            filme_randomico         = choice(lista_ultimos_filmes)
        
        frase                   = filme_randomico.frases
        filme                   = filme_randomico.titulo_nacional
        dados_escolhidos        = {'frase': frase, 'filme': filme}
        
        return dados_escolhidos