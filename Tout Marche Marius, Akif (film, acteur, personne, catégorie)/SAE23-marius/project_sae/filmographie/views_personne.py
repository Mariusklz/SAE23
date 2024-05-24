from django.shortcuts import render, redirect, get_object_or_404
from .models import Personne
from .forms import PersonneForm

def index(request):
    personne_form = PersonneForm()

    if request.method == 'POST':
        if 'ajouter_personne' in request.POST:
            personne_form = PersonneForm(request.POST)
            if personne_form.is_valid():
                personne_form.save()
                return redirect('index_personnes')

    personnes = Personne.objects.all()

    return render(request, 'filmographie/personnes/index.html', {
        'personne_form': personne_form,
        'personnes': personnes,
    })

def modifier(request, id):
    p = get_object_or_404(Personne, id=id)
    if request.method == 'POST':
        form = PersonneForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
            return redirect('index_personnes')
    else:
        form = PersonneForm(instance=p)
    return render(request, 'filmographie/personnes/modifier_personne.html', {'form': form})

def supprimer(request, id):
    personne = get_object_or_404(Personne, id=id)
    if request.method == 'POST':
        personne.delete()
        return redirect('index_personnes')
    return render(request, 'filmographie/personnes/supprimer_personne.html', {'personne': personne})

def affiche(request, id):
    personne = get_object_or_404(Personne, id=id)
    return render(request, "filmographie/personnes/affiche.html", {"personne": personne})
