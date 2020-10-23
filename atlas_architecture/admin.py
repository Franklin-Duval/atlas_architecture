from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Realisation)
admin.site.register(Service)
admin.site.register(Partenaire)
admin.site.register(Type)
admin.site.register(Caracteristique)
admin.site.register(ligneCaracteristique)
