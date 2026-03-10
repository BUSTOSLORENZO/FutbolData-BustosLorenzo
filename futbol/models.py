from django.db import models

class Liga(models.Model):

    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    temporada = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Club(models.Model):

    nombre = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Jugador(models.Model):

    nombre = models.CharField(max_length=50)
    posicion = models.CharField(max_length=30)
    edad = models.IntegerField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre