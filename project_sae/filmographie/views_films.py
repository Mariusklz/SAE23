from django.shortcuts import render
from .forms import FilmForm
from django.http import HttpResponseRedirect
from . import models

def index(request):
    liste = list(models.Film.objects.all())
    return render(request, "filmographie/films/index.html" , {"liste" : liste})


def ajout(request):
    if request.method == "POST":
        form = FilmForm(request.POST)
        return render(request,"filmographie/films/ajout.html",{"form": form})
    else :
        form = FilmForm()
    return render(request,"filmographie/films/ajout.html",{"form" : form})

def traitement(request):
    lform = FilmForm(request.POST)
    if lform.is_valid():
        film = lform.save()
        return render(request,"filmographie/films/affiche.html",{"film" : film})
    else:
        return render(request,"filmographie/films/ajout.html",{"form": lform})
    
def affiche(request, id):
    film = models.Film.objects.get(pk=id)
    return render(request,"filmographie/films/affiche.html",{"film": film})


def delete(request, id):
    film = models.Film.objects.get(pk=id)
    film.delete()
    return HttpResponseRedirect("/filmographie/")



def updatetraitement(request, id):
    film = models.Film.objects.get(pk=id)
    lform = FilmForm(request.POST, instance=film)
    if lform.is_valid():
        film = lform.save()
        return HttpResponseRedirect('/filmographie/films/')

def update(request, id):
    film = models.Film.objects.get(pk=id)
    form = FilmForm(film.catalogue())
    return render(request,"filmographie/films/ajout.html",{"form":form, "id": id})