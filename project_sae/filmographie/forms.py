from django import forms
from .models import Categorie, Personne

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['nom', 'descriptif']

class PersonneForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ['pseudo', 'nom', 'prenom', 'mail', 'mdp', 'type']