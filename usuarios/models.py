from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    biografia = models.TextField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)