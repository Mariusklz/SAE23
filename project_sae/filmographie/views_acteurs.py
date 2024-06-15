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
        form = ActeurForm(request.POST, request.FILES)
        return render(request,"filmographie/acteurs/ajout.html",{"form": form})
    else :
        form = ActeurForm()
    return render(request,"filmographie/acteurs/ajout.html",{"form" : form})

def traitement(request):
    aform = ActeurForm(request.POST, request.FILES)
    if aform.is_valid():
        acteur = aform.save()
        return render(request,"filmographie/acteurs/affiche.html",{"acteur" : acteur})
    else:
        return render(request,"filmographie/acteurs/ajout.html",{"form": aform})
    
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
    return HttpResponseRedirect("/acteurs/")



def updatetraitement(request, id):
    acteur = Acteur.objects.get(pk=id)
    aform = ActeurForm(request.POST, instance=acteur)
    if aform.is_valid():
        acteur = aform.save()
        return HttpResponseRedirect('/acteurs/')