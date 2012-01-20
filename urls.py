from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from r3play.settings import DEBUG

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'r3play.views.home', name='home'),
    # url(r'^r3play/', include('r3play.r3playapp.urls')),

    url(r'^adm1n/doc/', include('django.contrib.admindocs.urls')),
    url(r'^adm1n/', include(admin.site.urls)),

    url(r'^$', 'r3play.r3playapp.views.index', name='index'),
    url(r'^home/$', 'r3play.r3playapp.views.home', name='home'),
    url(r'^home/(?P<genero>\d+)$', 'r3play.r3playapp.views.home', name='home'),
    url(r'^filme/(?P<filme_id>\d+)/$', 'r3play.r3playapp.views.filme', name='filme'),
    url(r'^busca/$', 'r3play.r3playapp.views.busca', name='busca'),
    url(r'^categorias/$', 'r3play.r3playapp.views.categorias', name='categorias'),
    url(r'^artistas/$', 'r3play.r3playapp.views.artistas', name='artistas'),
    url(r'^artista/(?P<artista_id>\d+)/$', 'r3play.r3playapp.views.artista', name='artista'),
    url(r'^usuarios/$', 'r3play.r3playapp.views.usuarios', name='usuarios'),
    url(r'^cinemas/$', 'r3play.r3playapp.views.cinemas', name='cinemas'),
)

#handler404 = 'r3playapp.views.p404'