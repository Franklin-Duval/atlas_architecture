from django.db import models

# Create your models here.
class Partenaire(models.Model):
    logo = models.ImageField(null=True, blank=True, upload_to="images/partenaire")
    nom = models.CharField(max_length=150)
    description = models.TextField(null=True)
    email = models.EmailField(unique=True, null=False)

    def __str__(self):
        return self.nom

class Service(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField(null=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/service")

    def __str__(self):
        return self.nom
    

class Type(models.Model):
    nom = models.CharField(max_length=50, null=False)

    def __str___(self):
        return self.nom

class Caracteristique(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom
    

class Realisation(models.Model):
    code = models.CharField(max_length=10, unique=True, null=False)
    nom = models.CharField(max_length=100, null=False)
    date = models.DateField(null=False)
    lieu = models.CharField(max_length=25, null=False)
    description = models.TextField(null=True)
    types = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.code + " " + self.nom


class Image(models.Model):
    images = models.ImageField(null=True, blank=True, upload_to="images/realisation")
    realisation = models.ForeignKey(Realisation, on_delete=models.CASCADE)


class ligneCaracteristique(models.Model):
    realisation = models.ForeignKey(Realisation, on_delete=models.CASCADE, null=False)
    caracteristique = models.ForeignKey(Caracteristique, on_delete=models.CASCADE, null=False)
