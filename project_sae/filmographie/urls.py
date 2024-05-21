from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('modifier_categorie/<int:id>/', views.modifier_categorie, name='modifier_categorie'),
    path('supprimer_categorie/<int:id>/', views.supprimer_categorie, name='supprimer_categorie'),
    path('modifier_personne/<int:id>/', views.modifier_personne, name='modifier_personne'),
    path('supprimer_personne/<int:id>/', views.supprimer_personne, name='supprimer_personne'),
    
]
