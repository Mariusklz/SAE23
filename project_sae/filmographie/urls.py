from django.urls import path
from . import views

urlpatterns = [
    path('personnes/', views.index_personne, name='index'),
    path('categorie/', views.index_categorie, name='index'),
    path('categorie/modifier_categorie/<int:id>/', views.modifier_categorie, name='modifier_categorie'),
    path('categorie/supprimer_categorie/<int:id>/', views.supprimer_categorie, name='supprimer_categorie'),
    path('personnes/modifier_personne/<int:id>/', views.modifier_personne, name='modifier_personne'),
    path('personnes/supprimer_personne/<int:id>/', views.supprimer_personne, name='supprimer_personne'),
    
]
