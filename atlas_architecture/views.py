from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'acceuil.html')

def realisation(request):
    return render(request, 'realisation.html')

def partenaire(request):
    return render(request, 'partenaire.html')

def service(request):
    return render(request, 'service.html')
