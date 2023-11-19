
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    nombre = models.CharField(max_length = 200)


    def __str__(self):
        return self.nombre

class Hashtag(models.Model):
    nombre = models.CharField(max_length = 200)


    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length = 200)
    texto = models.TextField()
    fecha = models.DateTimeField(default = timezone.now)
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Category, on_delete = models.CASCADE)
    etiquetas = models.ManyToManyField(Hashtag)


def __str__(self):
    return (
        f"{self.titulo} "
        f"({self.autor.first_name} {self.autor.last_name})"
 )