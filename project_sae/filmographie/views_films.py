from django.shortcuts import render
from .forms import FilmForm
from django.http import HttpResponseRedirect
from .models import Film
from PIL import Image

##Marius
def index(request):
    liste = list(Film.objects.all())
    return render(request, "filmographie/films/index.html" , {"liste" : liste})


def ajout(request):
    if request.method == "POST":
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/films/")
        return render(request, "filmographie/films/ajout.html", {"form": form})
    else:
        form = FilmForm()
    return render(request, "filmographie/films/ajout.html", {"form": form})

def traitement(request):
    fform = FilmForm(request.POST, request.FILES)
    if fform.is_valid():
        film = fform.save()
        affiche = fform.cleaned_data.get('affiche')
        if affiche:
            img = Image.open(affiche)
            img.thumbnail((300, 300))
            img.save(film.affiche.path)
        return render(request,"filmographie/films/affiche.html",{"film" : film})
    else:
        return render(request,"filmographie/films/ajout.html",{"form": fform})
    
def affiche(request, id):
    film = Film.objects.get(pk=id)
    return render(request,"filmographie/films/affiche.html",{"film": film})


def delete(request, id):
    film = Film.objects.get(pk=id)
    film.delete()
    return HttpResponseRedirect("/films/")



def updatetraitement(request, id):
    film = Film.objects.get(pk=id)
    fform = FilmForm(request.POST, instance=film)
    if fform.is_valid():
        film = fform.save()
        return HttpResponseRedirect('/films/')

def update(request, id):
    film = Film.objects.get(pk=id)
    form = FilmForm(film.catalogue())
    return render(request,"filmographie/films/ajout.html",{"form":form, "id": id})