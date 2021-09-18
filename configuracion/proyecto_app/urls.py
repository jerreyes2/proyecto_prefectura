from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
   
   # Inicio
   # path('', views.index, name='index'),

   # Enlaces pagina
    
    
    path('',views.inicio, name="inicio"),
    
    path('administrar/', views.index, name='index'),
    path("administracion/",views.administracion, name="administracion"),

    path("especie/<int:id_fauna>",views.especie, name="especie"),

    path("flora/",views.flora, name="flora"),

    #path("fauna/",views.fauna, name="fauna"),
    path("fauna/<int:id_bioma>",views.fauna, name="fauna"),

    path("areasnat/",views.areasnat, name="areasnat"),

    path("infoweb/",views.infoweb, name="infoweb"),
    
    path("sugerencias/",views.sugerencias, name="sugerencias"),

    path("familia/",views.familia, name="familia"),

    path("subfamilia/",views.subfamilia, name="subfamilia"),

    #path("galeria/",views.galeria, name="galeria"),
    path('galeria/<int:id_fauna_biomas>/<int:tipo>', views.galeria, name="galeria"),
    #
    path("galeriabioma/", views.galeriabioma, name="galeriabioma"),
    
    
   
    
    

    
   # path('familia/list/', FamiliaListView.as_view(), name='category_list'),
]



# Ejemplo para los enlaces pagina
"""
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('store/', views.store, name="store"),
    path('contact/', views.contact, name="contact"),
    path('blog/', views.blog, name="blog"),
    path('sample/', views.sample, name="sample"),
]


"""
