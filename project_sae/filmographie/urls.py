from django.urls import path
from . import views

urlpatterns = [
    path('personnes/', views.index_personne, name='index_personnes'),
    path('categorie/', views.index_categorie, name='index_categorie'),
    path('categorie/afficher_categorie/<int:id>/', views.affiche_categorie, name='afficher_categorie'),
    path('categorie/modifier_categorie/<int:id>/', views.modifier_categorie, name='modifier_categorie'),
    path('categorie/supprimer_categorie/<int:id>/', views.supprimer_categorie, name='supprimer_categorie'),
    path('personnes/modifier_personne/<int:id>/', views.modifier_personne, name='modifier_personne'),
    path('personnes/supprimer_personne/<int:id>/', views.supprimer_personne, name='supprimer_personne'),
    path('categorie/afficher_personne/<int:id>/', views.affiche_personne, name='afficher_personne'),
]
