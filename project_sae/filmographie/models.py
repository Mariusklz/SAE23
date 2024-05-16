from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Films(models.Model):
    titre = models.CharField(max_length=100)
    annee_de_sortie = models.IntegerField(
        validators=[
           MinValueValidator(1895), # Premier film crée en 1895
           MaxValueValidator(9999)  
        ] 
    )
    affiche = models.ImageField(upload_to='affiches/', default=None, null = True, blank = True)
    realisateur = models.CharField(max_length=100)
    categorie = models.CharField(max_length=100)
    acteur = models.ForeignKey("acteur", on_delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f"Le Film {self.titre} est sortie en {self.annee_de_sortie} réalisé par {self.realisateur} de la catégorie {self.categorie}.{self.affiche}"
        return chaine

    def catalogue(self):
        return {"Titre":self.titre, "Année de sortie":self.annee_de_sortie, "Affiche":self.affiche,
                 "Réalisateur":self.realisateur, "Catégorie":self.categorie}

class Acteurs(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    photos = models.ImageField(upload_to='photos/', null = True, blank = True)

    def __str__(self):
        chaine = f"L'acteur' {self.nom} {self.prenom} à {self.age}.{self.photos}"
        return chaine

    def catalogue(self):
        return {"Nom":self.nom, "Prénom":self.prenom, "Age":self.age, "Photos":self.photos}
