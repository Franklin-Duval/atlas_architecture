from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'atlas_architecture/acceuil.html')

def realisation(request):
    return render(request, 'atlas_architecture/realisation.html')

def partenaire(request):
    return render(request, 'atlas_architecture/partenaire.html')

def service(request):
    return render(request, 'atlas_architecture/service.html')
