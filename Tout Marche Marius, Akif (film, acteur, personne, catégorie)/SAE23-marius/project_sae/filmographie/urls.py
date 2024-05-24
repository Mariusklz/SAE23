from django.urls import path
from . import views_films, views_acteurs, views_categorie, views_personne, views


urlpatterns = [

    ## liste des liens
    path('test/', views.index),

    #URLS Films
    path('', views_films.index),
    path('ajout/',views_films.ajout),
    path('traitement/', views_films.traitement),
    path('affiche/<int:id>/',views_films.affiche),
    path('update/<int:id>/',views_films.update),
    path('updatetraitement/<int:id>/',views_films.updatetraitement),
    path('delete/<int:id>/', views_films.delete),


    #URLS Acteur
    path('acteurs/', views_acteurs.index),
    path('acteurs/ajout/', views_acteurs.ajout),
    path('acteurs/traitement/', views_acteurs.traitement),
    path('acteurs/affiche/<int:id>/', views_acteurs.affiche),
    path('acteurs/update/<int:id>/',views_acteurs.update),
    path('acteurs/updatetraitement/<int:id>/',views_acteurs.updatetraitement),
    path('acteurs/delete/<int:id>/', views_acteurs.delete),


    #URLS Personnes
    path('personnes/', views_personne.index, name='index_personnes'),
    path('personnes/modifier_personne/<int:id>/', views_personne.modifier, name='modifier_personne'),
    path('personnes/supprimer_personne/<int:id>/', views_personne.supprimer, name='supprimer_personne'),
    path('personnes/afficher_personne/<int:id>/', views_categorie.affiche, name='afficher_personne'),


    #URLS Catégorie
    path('categorie/', views_categorie.index, name='index_categorie'),
    path('categorie/afficher_categorie/<int:id>/', views_categorie.affiche, name='afficher_categorie'),
    path('categorie/modifier_categorie/<int:id>/', views_categorie.modifier, name='modifier_categorie'),
    path('categorie/supprimer_categorie/<int:id>/', views_categorie.supprimer, name='supprimer_categorie'),
    
]