from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    descriptif = models.TextField()
    
    def __str__(self):
        return self.nom, self. descriptif

class Personne(models.Model):

    pseudo = models.CharField(max_length=100, unique=True)
    nom = models.CharField(max_length=100, unique=True)     
    prenom = models.CharField(max_length=100, unique=True)
    mail = models.EmailField(max_length=254, unique=True)
    mdp = models.CharField(max_length=100)
    TYPE_CHOICES = (
        ('professionnel', 'Professionnel'),
        ('amateur', 'Amateur'),
    )
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    def __str__(self):
        return self.pseudo,self.nom, self.prenom, self.mail, self.mdp, self.type