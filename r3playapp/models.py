#!/usr/bin/env python
# encoding: utf-8

from django.db import models
from thumbs import ImageWithThumbsField

    
class Generos(models.Model):
    nome                    = models.CharField(max_length = 200)
    descricao               = models.TextField(blank=True, null=True)
    
    class Meta:
                   verbose_name_plural = u'Gêneros'
    
    def __unicode__(self):
        return self.nome

class Artistas(models.Model):
    nome                    = models.CharField(max_length = 200)
    data_nascimento         = models.DateField()
    pais                    = models.CharField(max_length = 100)
    cidade_natal            = models.CharField(max_length = 100, blank=True, null=True)
    #foto                    = models.ImageField(upload_to='upload/artistas/%Y/%m/%d')
    foto                    = ImageWithThumbsField( upload_to='upload/artistas/%Y/%m/%d', sizes=((80,80),) )
    
    class Meta:
                   verbose_name_plural = "Artistas"
    
    def __unicode__(self):
        return self.nome
    
class Diretores(models.Model):
    nome                    = models.CharField(max_length = 200)
    data_nascimento         = models.DateField()
    pais                    = models.CharField(max_length = 100)
    cidade_natal            = models.CharField(max_length = 100, blank=True, null=True)
    #foto                    = models.ImageField(upload_to='upload/diretores/%Y/%m/%d')
    foto                    = ImageWithThumbsField( upload_to='upload/diretores/%Y/%m/%d', sizes=((80,80),) )
    
    class Meta:
                   verbose_name_plural = "Diretores"
    
    def __unicode__(self):
        return self.nome

class Filmes(models.Model):
    TIPO_ESCOLHAS = (
        ('em breve', 'Em breve'),
        ('cinema', 'Cinema'),
        ('dvd & blueray', 'DVD & BLURAY')
    )
    ORIGEM_ESCOLHAS = (
        ('internacional', 'INTERNACIONAL'),
        ('nacional', 'NACIONAL')
    )

    tipo                    = models.CharField(max_length = 30, choices=TIPO_ESCOLHAS)
    estreia                 = models.DateField(blank=True, null=True)
    titulo_original         = models.CharField(max_length = 200, verbose_name='Título original')
    titulo_nacional         = models.CharField(max_length = 200, verbose_name='Título nac.')
    ano_lancamento          = models.DecimalField(verbose_name='Ano', max_digits=4, decimal_places=0)
    duracao                 = models.IntegerField(verbose_name='Minutos')
    idade_classificacao     = models.IntegerField(blank=True, null=True, verbose_name='Idade')
    estudio                 = models.CharField(max_length = 50, blank=True, null=True, verbose_name='Estúdio')
    sinopse                 = models.TextField()
    genero                  = models.ManyToManyField(Generos)
    diretores               = models.CharField(max_length = 400)
    artistas                = models.TextField()
    #frases                  = models.TextField(blank=True, verbose_name='Frase')
    trailer                 = models.TextField(blank=True, verbose_name='Trailer')
    #capa                    = models.ImageField(upload_to='upload/filmes/%Y/%m/%d') 
    capa                    = ImageWithThumbsField( upload_to='upload/filmes/%Y/%m/%d', sizes=((124,184),(115,170)) )
    origem                  = models.CharField(max_length = 50, choices=ORIGEM_ESCOLHAS, default='internacional')
    
    class Meta:
                   verbose_name_plural = "Filmes"
                   
    def __unicode__(self):
        return self.titulo_nacional


class Categorias(models.Model):
    nome                    = models.CharField(max_length = 200)
    resenha                 = models.TextField()
    #foto                    = models.ImageField(upload_to='upload/categorias/%Y/%m/%d')
    foto                    = ImageWithThumbsField( upload_to='upload/categorias/%Y/%m/%d', sizes=((186,155),) )
    filmes                  = models.ManyToManyField(Filmes)

    class Meta:
        verbose_name_plural = "Categorias"

    def __unicode__(self):
        return self.nome
        
class Frases(models.Model):
    frase                   = models.TextField()
    filmes                  = models.ManyToManyField( Filmes )
    
    class Meta:
        verbose_name_plural = "Frases"
    
    def __unicode__(self):
        return self.frase

class Cinemas(models.Model):
    nome                    = models.CharField(max_length = 100)
    rede                    = models.CharField(max_length = 100, null=True, blank=True, verbose_name='Rede Cinema')
    cep                     = models.IntegerField(null=True, blank=True, verbose_name='CEP')
    endereco                = models.CharField(max_length = 300, verbose_name='Endereço')
    bairro                  = models.CharField(max_length = 100, null=True, blank=True)
    cidade                  = models.CharField(max_length = 100)
    estado                  = models.CharField(max_length = 100)
    shopping                = models.CharField(max_length = 100, null=True, blank=True)
    telefone                = models.CharField(max_length = 100, null=True, blank=True)
    site                    = models.URLField(max_length = 200, null=True, blank=True)
    email                   = models.EmailField(max_length = 200, null=True, blank=True)
    logomarca               = ImageWithThumbsField( upload_to='upload/logomarcas/%Y/%m/%d', sizes=( (171,104), (80,80), (44,44),) )
    
    class Meta:
        verbose_name_plural = "Cinemas"
    
    def __unicode__(self):
        return self.nome