from django.contrib import admin

from posts.models import Posteo


@admin.register(Posteo)
class PosteoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "fecha_publicacion")
    search_fields = ("titulo", "autor", "contenido")
    list_filter = ("fecha_publicacion",)
