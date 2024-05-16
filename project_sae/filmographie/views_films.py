from django.shortcuts import render
from .forms import FilmsForm
from django.http import HttpResponseRedirect
from . import models


def index(request):
    return render(request, "filmographie/films/index.html" )


def ajout(request):
    if request.method == "POST":
        form = FilmsForm(request.POST)
        return render(request,"filmographie/films/ajout.html",{"form": form})
    else :
        form = FilmsForm()
    return render(request,"filmographie/films/ajout.html",{"form" : form})

def traitement(request):
    lform = FilmsForm(request.POST)
    if lform.is_valid():
        films = lform.save()
        return render(request,"filmographie/films/affiche.html",{"films" : films})
    else:
        return render(request,"filmographie/films/ajout.html",{"form": lform})
    
def affiche(request, id):
    films = models.Films.objects.get(pk=id)
    return render(request,"filmographie/films/affiche.html",{"films": films})
