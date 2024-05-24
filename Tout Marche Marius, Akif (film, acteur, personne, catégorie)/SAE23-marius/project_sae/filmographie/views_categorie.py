from django.shortcuts import render, redirect, get_object_or_404
from .models import Categorie
from .forms import CategorieForm




def index(request):
    categorie_form = CategorieForm()

    if request.method == 'POST':
        if 'ajouter_categorie' in request.POST:
            categorie_form = CategorieForm(request.POST)
            if categorie_form.is_valid():
                categorie_form.save()
                return redirect('index_categorie')

    categories = Categorie.objects.all()

    return render(request, 'filmographie/categorie/index.html', {
        'categorie_form': categorie_form,
        'categories': categories,
    })

def modifier(request, id):
    categorie = get_object_or_404(Categorie, id=id)
    if request.method == 'POST':
        form = CategorieForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            return redirect('index_categorie')
    else:
        form = CategorieForm(instance=categorie)
    return render(request, 'filmographie/categorie/modifier_categorie.html', {'form': form})

def supprimer(request, id):
    categorie = get_object_or_404(Categorie, id=id)
    if request.method == 'POST':
        categorie.delete()
        return redirect('index_categorie')
    return render(request, 'filmographie/categorie/supprimer_categorie.html', {'categorie': categorie})



def affiche(request, id):
    categorie = get_object_or_404(Categorie, id=id)
    return render(request, "filmographie/categorie/affiche.html", {"categorie": categorie})
    