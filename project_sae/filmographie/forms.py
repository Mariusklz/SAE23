from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Film, Acteur

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
