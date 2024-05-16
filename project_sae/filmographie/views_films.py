from django.shortcuts import render
from .forms import FilmsForm
from django.http import HttpResponseRedirect
from . import models


def index(request):
    return render(request, "filmographie/films/index.html" )


def ajout(request, id):
    if request.method == "POST":
        form = FilmsForm(request.POST)
        return render(request,"filmographie/films/ajout.html",{"form": form, "id_a": id})
    else :
        form = FilmsForm()
    return render(request,"filmographie/films/ajout.html",{"form" : form, "id_a": id})

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

def update(request, id):
    film = models.Films.objects.get(pk=id)
    form = FilmsForm(film.catalogue())
    return render(request,"filmographie/films/ajout.html",{"form":form, "id_f": id})


def delete(request, id):
    film = models.Films.objects.get(pk=id)
    film.delete()
    return HttpResponseRedirect("/filmographie/films/")
