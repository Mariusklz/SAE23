from django.urls import path
from . import views

urlpatterns = [
    path('personnes/', views.index_personne, name='index'),
    path('categorie/', views.index_categorie, name='index'),
    path('modifier_categorie/categorie/<int:id>/', views.modifier_categorie, name='modifier_categorie'),
    path('supprimer_categorie/categorie/<int:id>/', views.supprimer_categorie, name='supprimer_categorie'),
    path('modifier_personne/personnes/<int:id>/', views.modifier_personne, name='modifier_personne'),
    path('supprimer_personne/personnes/<int:id>/', views.supprimer_personne, name='supprimer_personne'),
    
]
