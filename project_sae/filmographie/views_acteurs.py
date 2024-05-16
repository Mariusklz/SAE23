from django.shortcuts import render
from .forms import ActeursForm
from django.http import HttpResponseRedirect
from . import models


def index(request):
    return render(request, "filmographie/acteurs/index.html" )


def ajout(request):
    if request.method == "POST":
        form = ActeursForm(request.POST)
        return render(request,"filmographie/acteurs/ajout.html",{"form": form})
    else :
        form = ActeursForm()
    return render(request,"filmographie/acteurs/ajout.html",{"form" : form})

def traitement(request):
    lform = ActeursForm(request.POST)
    if lform.is_valid():
        pays = lform.save()
        return render(request,"filmographie/acteurs/affiche.html",{"pays" : pays})
    else:
        return render(request,"filmographie/acteurs/ajout.html",{"form": lform})
    
def affiche(request, id):
    acteur = models.Acteurs.objects.get(pk=id)
    return render(request,"filmographie/acteurs/affiche.html",{"acteur": acteur})
