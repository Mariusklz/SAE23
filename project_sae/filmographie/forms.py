from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Films, Acteurs

class FilmsForm(ModelForm):
    class Meta:
        model = Films
        fields = ('titre', 'annee_de_sortie', 'affiche', 'realisateur', 'categorie')
        labels = {
            'titre': _('Titre du Film'),
            'annee_de_sortie': _('Année de sortie du Film'),
            'realisateur': _('Réalisateur du Film'),
            'categorie': _('Catégorie du Film'),
            'affiche': _('Affiche du Film'),
        }


class ActeursForm(ModelForm):
    class Meta:
        model = Acteurs
        fields = ('nom', 'prenom', 'age', 'photos')
        labels = {
            'nom': _("Nom de l'Acteur"),
            'prenom': _("Prénom de l'Acteur"),
            'age': _("Age de l'Acteur"),
            'photos': _("Photos de l'Acteur"),
        }
