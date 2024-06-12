from django.shortcuts import render
from .forms import CommentaireForm
from django.http import HttpResponseRedirect
from .models import Commentaire

#Greg
def index(request):
    liste = list(Commentaire.objects.all())
    return render(request, "filmographie/commentaires/index.html" , {"liste" : liste})


def ajout(request):
    if request.method == "POST":
        form = CommentaireForm(request.POST)
        return render(request,"filmographie/commentaires/ajout.html",{"form": form})
    else :
        form = CommentaireForm()
    return render(request,"filmographie/commentaires/ajout.html",{"form" : form})

def traitement(request):
    cform = CommentaireForm(request.POST)
    if cform.is_valid():
        commentaire = cform.save()
        return render(request,"filmographie/commentaires/affiche.html",{"commentaire" : commentaire})
    else:
        return render(request,"filmographie/commentaires/ajout.html",{"form": cform})
    
def affiche(request, id):
    commentaire = Commentaire.objects.get(pk=id)
    return render(request,"filmographie/commentaires/affiche.html",{"commentaire": commentaire})


def update(request, id):
    commentaire = Commentaire.objects.get(pk=id)
    form = CommentaireForm(commentaire.catalogue())
    return render(request,"filmographie/commentaires/ajout.html",{"form":form, "id": id})



def delete(request, id):
    commentaire = Commentaire.objects.get(pk=id)
    commentaire.delete()
    return HttpResponseRedirect("/filmographie/commentaires/")



def updatetraitement(request, id):
    commentaire = Commentaire.objects.get(pk=id)
    cform = CommentaireForm(request.POST, instance=commentaire)
    if cform.is_valid():
        commentaire = cform.save()
        return HttpResponseRedirect('/filmographie/commentaires/')