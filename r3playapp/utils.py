#!/usr/bin/env python
# encoding: utf-8

from r3play.r3playapp.models import Frases
from random import choice

class Util:
    def __init__(self):
        pass
        
    def frase_randomica(self):
        lista_frases            = Frases.objects.all()
        frase_aleatoria         = choice(lista_frases)
        dados_escolhidos        = {'frase': frase_aleatoria.frase, 'filme': frase_aleatoria.filmes.all()[0]}
        
        return dados_escolhidos