from typing import Iterable

from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=50)
    contenido = models.TextField()
    fecha_publicacion = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Post ({self.id}): {self.titulo} - Autor: {self.autor}"