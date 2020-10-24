from django.urls import path

from . import views

urlpatterns = [
    path('acceuil', views.home, name='home'),
    path('realisation', views.realisation, name='realisation'),
    path('partenaire', views.partenaire, name='partenaire'),
    path('service', views.service, name='service'),
]