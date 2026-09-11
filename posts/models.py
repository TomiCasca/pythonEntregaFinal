from django.db import models

class Posteo(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=50)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='posteo', null=True)
    fecha_publicacion = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Post ({self.id}): {self.titulo} - Autor: {self.autor}"