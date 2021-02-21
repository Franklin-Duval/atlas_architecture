from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('acceuil', views.home, name='home'),
    path('realisation', views.realisation, name='realisation'),
    path('partenaire', views.partenaire, name='partenaire'),
    path('service', views.service, name='service'),
    path('', views.root, name='root'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)