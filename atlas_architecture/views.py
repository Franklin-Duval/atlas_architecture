from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, 'atlas_architecture/acceuil.html')

def realisation(request):
    details = []
    realisations = Realisation.objects.all()
    ligne = ligneCaracteristique.objects.all()
    images = Image.objects.all()

    for real in realisations:
        obj = {
            "realisations": real,
            "images": [],
            "xtics": []
        }
        for im in images:
            if im.realisation.code == real.code:
                obj["images"].append(im.images)
        
        for xtics in ligne:
            if (xtics.realisation.code == real.code):
                obj["xtics"].append(xtics.caracteristique.nom)
        
        details.append(obj)

    context = {"content": details}
    #print("\n\n", context, "\n\n")
    return render(request, 'atlas_architecture/realisation.html', context)

def partenaire(request):
    return render(request, 'atlas_architecture/partenaire.html')

def service(request):
    services = Service.objects.all()
    context = {"services": services}
    return render(request, 'atlas_architecture/service.html', context)
