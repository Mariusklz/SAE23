from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Film, Acteur, Categorie, Personne, Commentaire

##Marius

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ('titre', 'annee_de_sortie', 'affiche', 'realisateur')
        labels = {
            'titre': _('Titre du Film'),
            'annee_de_sortie': _('Année de sortie du Film'),
            'realisateur': _('Réalisateur du Film'),
            'affiche': _('Affiche du Film'),
        }


class ActeurForm(ModelForm):
    class Meta:
        model = Acteur
        fields = ('nom', 'prenom', 'age', 'photos')
        labels = {
            'nom': _("Nom de l'Acteur"),
            'prenom': _("Prénom de l'Acteur"),
            'age': _("Age de l'Acteur"),
            'photos': _("Photos de l'Acteur"),
        }

##AKIF
class CategorieForm(ModelForm):
    class Meta:
        model = Categorie
        fields = ('nom', 'descriptif')
        labels = {
            'nom_categorie': _("Nom de la Catégorie"),
            'descriptif': _("Déscriptif de la catégorie"),
        }

class PersonneForm(ModelForm):
    class Meta:
        model = Personne
        fields = ('pseudo', 'nom', 'prenom', 'mail', 'mdp', 'type')
        labels = {
            "pseudo": _("Pseudo de la Personne"),
            "nom_personne": _("Nom de la Personne"),
        }

#Marius
class CommentaireForm(ModelForm):
    class Meta:
        model = Commentaire
        fields = ('note', 'commentaire', 'date', 'film', 'personne')
        labels = {
            'note': _("Note"),
            'commentaire': _("Commentaire"),
            'date': _("Date du Commentaire"),
            'film': _("film"),
            'personne': _("personne")
        }