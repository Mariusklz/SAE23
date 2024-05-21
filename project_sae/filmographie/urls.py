from django.urls import path
from . import views_films, views_acteurs


urlpatterns = [
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
    path('acteurs/update/<int:id>/',views_films.update),
    path('acteurs/updatetraitement/<int:id>/',views_films.updatetraitement),
    path('acteurs/delete/<int:id>/', views_films.delete),
]