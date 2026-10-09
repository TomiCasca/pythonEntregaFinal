from django import forms

from posts.models import Posteo


class FormularioPosteo(forms.ModelForm):
    """Formulario único para crear y editar un posteo (incluye la imagen)."""

    class Meta:
        model = Posteo
        fields = "__all__"
