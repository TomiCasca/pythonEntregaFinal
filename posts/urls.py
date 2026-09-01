from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("posts/", views.lista_posts, name="lista_posts"),
    path("posts/<int:post_id>/", views.detalle_post, name="detalle_post"),
    path("contacto/", views.contacto, name="contacto"),
]