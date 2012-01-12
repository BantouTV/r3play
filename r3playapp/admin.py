from django.contrib import admin
from r3playapp.models import Filmes
from r3playapp.models import Diretores
from r3playapp.models import Artistas
from r3playapp.models import Categorias
from r3playapp.models import Generos

class ArtistasAdmin(admin.ModelAdmin):
    list_display            = ('nome', 'data_nascimento', 'cidade_natal')
    list_filter             = ('pais',)
    search_fields           = ['nome',]

admin.site.register(Artistas, ArtistasAdmin)

class DiretoresAdmin(admin.ModelAdmin):
    list_display            = ('nome', 'data_nascimento', 'cidade_natal')
    list_filter             = ('pais',)
    search_fields           = ['nome',]
    
admin.site.register(Diretores, DiretoresAdmin)

class FilmesAdmin(admin.ModelAdmin):
    ordering                = ['titulo_nacional', 'ano_lancamento', 'titulo_original',]
    #date_hierarchy          = 'ano_lancamento'
    fieldsets = (
            (None, {
                'fields': ('tipo', 
                            'estreia', 
                            'titulo_nacional', 
                            'titulo_original', 
                            'ano_lancamento', 
                            'duracao',
                            'idade_classificacao', 
                            'estudio', 
                            'genero', 
                            'sinopse', 
                            'diretores', 
                            'artistas', 
                            'frases', 
                            'capa', 
                            'origem', 
                            )
            }),
        )
    list_display            = ('titulo_nacional', 'titulo_original',)
    list_filter             = ('genero', 'estreia')
    search_fields           = ['titulo_original', 'titulo_nacional']
    radio_fields            = {"origem": admin.HORIZONTAL}
    filter_horizontal       = ("genero",) # box para filtar multiplas selecoes

admin.site.register(Filmes, FilmesAdmin)

class CategoriasAdmin(admin.ModelAdmin):
    list_display            = ('nome', 'resenha',)
    filter_horizontal       = ("filmes",)
    
admin.site.register(Categorias, CategoriasAdmin)

class GenerosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    
admin.site.register(Generos, GenerosAdmin)

