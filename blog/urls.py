from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'', views.pelicula_nueva, name='pelicula_nueva'),
    #url(r'^pelicula/nueva/$', views.pelicula_nueva, name='pelicula_nueva'),
]
