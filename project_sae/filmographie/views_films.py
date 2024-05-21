from django.shortcuts import render
from .forms import FilmForm
from django.http import HttpResponseRedirect
from . import models


def index(request):
    liste = list(models.Film.objects.all())
    return render(request, "filmographie/films/index.html" , {"liste" : liste, "id": id})


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
        films = lform.save()
        return render(request,"filmographie/films/affiche.html",{"films" : films})
    else:
        return render(request,"filmographie/films/ajout.html",{"form": lform})
    
def affiche(request, id):
    films = models.Film.objects.get(pk=id)
    return render(request,"filmographie/films/affiche.html",{"films": films})

def update(request, id):
    films = models.Film.objects.get(pk=id)
    form = FilmForm(films.catalogue())
    return render(request,"filmographie/films/ajout.html",{"form":form, "id": id})


def delete(request, id):
    films = models.Film.objects.get(pk=id)
    films.delete()
    return HttpResponseRedirect("/filmographie/films/")




def updatetraitement(request, id):
    films = models.Film.objects.get(pk=id)
    lform = FilmForm(request.POST, instance=films)
    if lform.is_valid():
        films = lform.save()
        return HttpResponseRedirect('/filmographie/')
