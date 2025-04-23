from django.db import models

# Create your models here.

class Recomendacion(models.Model):
    titulo = models.CharField(max_length=200)
    resumen = models.TextField()
    nombre_usuario = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.titulo




class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    resumen = models.TextField()
    fecha_de_publicacion = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=200, blank=True, null=True)
    imagen = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.titulo
