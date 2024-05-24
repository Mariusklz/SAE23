from django.shortcuts import render
from .forms import ActeurForm
from django.http import HttpResponseRedirect
from .models import Acteur

##Marius
def index(request):
    liste = list(Acteur.objects.all())
    return render(request, "filmographie/acteurs/index.html" , {"liste" : liste})


def ajout(request):
    if request.method == "POST":
        form = ActeurForm(request.POST)
        return render(request,"filmographie/acteurs/ajout.html",{"form": form})
    else :
        form = ActeurForm()
    return render(request,"filmographie/acteurs/ajout.html",{"form" : form})

def traitement(request):
    lform = ActeurForm(request.POST)
    if lform.is_valid():
        acteur = lform.save()
        return render(request,"filmographie/acteurs/affiche.html",{"acteur" : acteur})
    else:
        return render(request,"filmographie/acteurs/ajout.html",{"form": lform})
    
def affiche(request, id):
    acteur = Acteur.objects.get(pk=id)
    return render(request,"filmographie/acteurs/affiche.html",{"acteur": acteur})


def update(request, id):
    acteur = Acteur.objects.get(pk=id)
    form = ActeurForm(acteur.catalogue())
    return render(request,"filmographie/acteurs/ajout.html",{"form":form, "id": id})



def delete(request, id):
    acteur = Acteur.objects.get(pk=id)
    acteur.delete()
    return HttpResponseRedirect("/filmographie/acteurs/")



def updatetraitement(request, id):
    acteur = Acteur.objects.get(pk=id)
    lform = ActeurForm(request.POST, instance=acteur)
    if lform.is_valid():
        acteur = lform.save()
        return HttpResponseRedirect('/filmographie/acteurs/')