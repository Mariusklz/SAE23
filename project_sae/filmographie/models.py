from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser


## Marius

class Film(models.Model):
    titre = models.CharField(max_length=100)
    annee_de_sortie = models.IntegerField(
        validators=[
           MinValueValidator(1895), # Premier film crée en 1895
           MaxValueValidator(9999)  
        ] 
    )
    affiche = models.ImageField(upload_to='affiche/', default=None, null = True, blank = True)
    realisateur = models.CharField(max_length=100)
    
    
    def __str__(self):
        chaine = f"Le Film {self.titre} est sortie en {self.annee_de_sortie} réalisé par {self.realisateur}.{self.affiche}"
        return chaine

    def catalogue(self):
        return {"titre":self.titre, "annee_de_sortie":self.annee_de_sortie, "affiche":self.affiche,
                 "realisateur":self.realisateur,}

class Acteur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    photos = models.ImageField(upload_to='photos/', null = True, blank = True)

    def __str__(self):
        chaine = f"L'acteur' {self.nom} {self.prenom} à {self.age}.{self.photos}"
        return chaine

    def catalogue(self):
        return {"nom":self.nom, "prenom":self.prenom, "age":self.age, "photos":self.photos}

## Akif
class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    descriptif = models.TextField()
 
    def __str__(self):
        return f"nom_categorie: {self.nom}, descriptif: {self.descriptif}"
    
    def catalogue(self):
        return {"nom_categorie":self.nom, "descriptif":self.descriptif}

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
        return f"pseudo: {self.pseudo}, nom_personne: {self.nom}, prenom_personne: {self.prenom}, mail: {self.mail}, mdp: {self.mdp}, type: {self.type}"
    
    def catalogue(self):
        return {"pseudo":self.pseudo, "nom_personne":self.nom, "prenom_personne":self.prenom, "mail":self.mail, "mdp":self.mdp, "type":self.type}



## Marius
class Commentaire(models.Model):
    note = models.IntegerField(
        validators=[
           MinValueValidator(0), #Note Minimum
           MaxValueValidator(10)  #Note Maximum
        ] 
    )
    commentaire = models.TextField()
    date = models.DateField()
    film = models.ForeignKey(Film, on_delete=models.CASCADE, default=None)
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return f"note: {self.note}, commentaire: {self.commentaire}, date: {self.date}"
    
    def catalogue(self):
        return {"note":self.note, "date":self.date, "film":self.film, "personne":self.personne, "commentaire":self.commentaire}