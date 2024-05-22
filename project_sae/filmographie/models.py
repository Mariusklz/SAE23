from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Film(models.Model):
    titre = models.CharField(max_length=100)
    annee_de_sortie = models.IntegerField(
        validators=[
           MinValueValidator(1895), # Premier film crée en 1895
           MaxValueValidator(9999)  
        ] 
    )
    affiche = models.ImageField(upload_to='affiches/', default=None, null = True, blank = True)
    realisateur = models.CharField(max_length=100)
    
    
    def __str__(self):
        chaine = f"Le Film {self.titre} est sortie en {self.annee_de_sortie} réalisé par {self.realisateur} de la catégorie.{self.affiche}"
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
