from django.db import models
from django.core.validators import FileExtensionValidator

class Filmes(models.Model):
    titulo = models.CharField(max_length=100)
    elenco = models.CharField(max_length=100)
    gênero = models.CharField(max_length=100,blank=True)
    capa = models.ImageField(upload_to='capas/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'webp'])])

    def __str__(self):
        return f"{self.titulo} {self.elenco}"

class Playlist(models.Model):
    nome = models.CharField(max_length=100)
    filmes = models.ManyToManyField(Filmes) 

    def __str__(self):
        return self.nome