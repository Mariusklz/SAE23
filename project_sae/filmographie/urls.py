from django.urls import path
from . import views_films, views_acteurs, views_categorie, views_personne, views, views_commentaires



urlpatterns = [

    ## liste des liens
    path('', views.index, name='index'),

    #URLS Films
    path('films/', views_films.index, name='index_films'),
    path('films/ajout/',views_films.ajout, name='ajout_films'),
    path('films/traitement/', views_films.traitement, name='traitement_films'),
    path('films/affiche/<int:id>/',views_films.affiche, name='affiche_films'),
    path('films/update/<int:id>/',views_films.update, name='update_films'),
    path('films/updatetraitement/<int:id>/',views_films.updatetraitement, name='updatetraitement_films'),
    path('films/delete/<int:id>/', views_films.delete, name='delete_films'),


    #URLS Acteur
    path('acteurs/', views_acteurs.index, name='index_acteurs'),
    path('acteurs/ajout/', views_acteurs.ajout, name='ajout_acteurs'),
    path('acteurs/traitement/', views_acteurs.traitement, name='traitement_acteurs'),
    path('acteurs/affiche/<int:id>/', views_acteurs.affiche, name='affiche_acteurs'),
    path('acteurs/update/<int:id>/',views_acteurs.update, name='update_acteurs'),
    path('acteurs/updatetraitement/<int:id>/',views_acteurs.updatetraitement, name='updatetraitement_acteurs'),
    path('acteurs/delete/<int:id>/', views_acteurs.delete, name='delete_acteurs'),


    #URLS Personnes
    path('personnes/', views_personne.index, name='index_personne'),
    path('personnes/modifier_personne/<int:id>/', views_personne.modifier, name='modifier_personne'),
    path('personnes/supprimer_personne/<int:id>/', views_personne.supprimer, name='supprimer_personne'),
    path('personnes/afficher_personne/<int:id>/', views_categorie.affiche, name='afficher_personne'),


    #URLS Catégorie
    path('categorie/', views_categorie.index, name='index_categorie'),
    path('categorie/afficher_categorie/<int:id>/', views_categorie.affiche, name='afficher_categorie'),
    path('categorie/modifier_categorie/<int:id>/', views_categorie.modifier, name='modifier_categorie'),
    path('categorie/supprimer_categorie/<int:id>/', views_categorie.supprimer, name='supprimer_categorie'),

    #URLS Commentaires
    path('commentaire/', views_commentaires.index, name='index_commentaires'),
    path('commentaire/ajout/',views_commentaires.ajout, name='ajout_commentaires'),
    path('commentaire/traitement/', views_commentaires.traitement, name='traitement_commentaires'),
    path('commentaire/affiche/<int:id>/',views_commentaires.affiche, name='affiche_commentaires'),
    path('commentaire/update/<int:id>/',views_commentaires.update, name='update_commentaires'),
    path('commentaire/updatetraitement/<int:id>/',views_commentaires.updatetraitement, name='updatetraitement_commentaires'),
    path('commentaire/delete/<int:id>/', views_commentaires.delete, name='delete_commentaires'),
    
]