from django.shortcuts import render
from .forms import FilmForm
from django.http import HttpResponseRedirect
from .models import Film

##Marius
def index(request):
    liste = list(Film.objects.all())
    return render(request, "filmographie/films/index.html" , {"liste" : liste})


def ajout(request):
    if request.method == "POST":
        form = FilmForm(request.POST)
        return render(request,"filmographie/films/ajout.html",{"form": form})
    else :
        form = FilmForm()
    return render(request,"filmographie/films/ajout.html",{"form" : form})

def traitement(request):
    fform = FilmForm(request.POST)
    if fform.is_valid():
        film = fform.save()
        return render(request,"filmographie/films/affiche.html",{"film" : film})
    else:
        return render(request,"filmographie/films/ajout.html",{"form": fform})
    
def affiche(request, id):
    film = Film.objects.get(pk=id)
    return render(request,"filmographie/films/affiche.html",{"film": film})


def delete(request, id):
    film = Film.objects.get(pk=id)
    film.delete()
    return HttpResponseRedirect("/filmographie/")



def updatetraitement(request, id):
    film = Film.objects.get(pk=id)
    fform = FilmForm(request.POST, instance=film)
    if fform.is_valid():
        film = fform.save()
        return HttpResponseRedirect('/filmographie/films/')

def update(request, id):
    film = Film.objects.get(pk=id)
    form = FilmForm(film.catalogue())
    return render(request,"filmographie/films/ajout.html",{"form":form, "id": id})