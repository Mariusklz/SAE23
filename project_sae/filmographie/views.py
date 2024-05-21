from django.shortcuts import render, redirect, get_object_or_404
from .models import Personne, Categorie
from .forms import PersonneForm, CategorieForm

def index(request):
    categorie_form = CategorieForm()
    personne_form = PersonneForm()

    if request.method == 'POST':
        if 'ajouter_categorie' in request.POST:
            categorie_form = CategorieForm(request.POST)
            if categorie_form.is_valid():
                categorie_form.save()
                return redirect('index')
        elif 'ajouter_personne' in request.POST:
            personne_form = PersonneForm(request.POST)
            if personne_form.is_valid():
                personne_form.save()
                return redirect('index')

    categories = Categorie.objects.all()
    personnes = Personne.objects.all()

    return render(request, 'filmographie/index.html', {
        'categorie_form': categorie_form,
        'personne_form': personne_form,
        'categories': categories,
        'personnes': personnes,
    })

def modifier_categorie(request, id):
    categorie = get_object_or_404(Categorie, id=id)
    if request.method == 'POST':
        form = CategorieForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategorieForm(instance=categorie)
    return render(request, 'filmographie/modifier_categorie.html', {'form': form})

def supprimer_categorie(request, id):
    categorie = get_object_or_404(Categorie, id=id)
    if request.method == 'POST':
        categorie.delete()
        return redirect('index')
    return render(request, 'filmographie/supprimer_categorie.html', {'categorie': categorie})

def modifier_personne(request, id):
    personne = get_object_or_404(Personne, id=id)
    if request.method == 'POST':
        form = PersonneForm(request.POST, instance=personne)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = Personne(instance=personne)
    return render(request, 'filmographie/modifier_personne.html', {'form': form})

def supprimer_personne(request, id):
    personne = get_object_or_404(Personne, id=id)
    if request.method == 'POST':
        personne.delete()
        return redirect('index')
    return render(request, 'filmographie/supprimer_filmographie.html', {'personne': personne})
