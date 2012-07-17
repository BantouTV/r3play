#!/usr/bin/env python
# encoding: utf-8

from r3play.r3playapp.models import Frases
from random import choice
from r3play.r3playapp.models import Filmes
from django.shortcuts import get_object_or_404

class Util:
    def __init__(self):
        pass
        
    def frase_randomica(self):
        lista_frases            = Frases.objects.all()
        frase_aleatoria         = choice(lista_frases)
        dados_escolhidos        = {
                                    'frase':    frase_aleatoria.frase, 
                                    'filme':    frase_aleatoria.filmes.all()[0],
                                    'id':       frase_aleatoria.filmes.all()[0].pk
                                }
        
        print frase_aleatoria
        print dados_escolhidos

        return dados_escolhidos
        
    def lista_paises(lista, self):
        pass
        
    def lista_alfabeto(self):
        alfabeto                    = []
        codes                       = range(ord('a'), ord('z')+1)
        
        for code in codes:
            alfabeto.append( chr(code) )
            
        return alfabeto
        
    def monta_lista_artistas_urls(artistas, self):
        pass