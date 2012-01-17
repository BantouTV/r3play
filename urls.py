from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'r3play.views.home', name='home'),
    # url(r'^r3play/', include('r3play.r3playapp.urls')),

    url(r'^adm1n/doc/', include('django.contrib.admindocs.urls')),
    url(r'^adm1n/', include(admin.site.urls)),
    
    url(r'^$', 'r3play.r3playapp.views.index', name='index'),
    url(r'^home/$', 'r3play.r3playapp.views.home', name='home'),
    url(r'^filme/(?P<filme_id>\d+)/$', 'r3play.r3playapp.views.filme', name='filme'),
    url(r'^busca/$', 'r3play.r3playapp.views.busca', name='busca'),
)
