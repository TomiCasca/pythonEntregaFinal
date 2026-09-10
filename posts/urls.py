from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("contacto/", views.contacto, name="contacto"),
    path("posts/", views.lista_posts, name="lista_posts"),
    path("posts/crear/", views.crear_post, name="crear_post"),
    path("posts/<int:post_id>/", views.detalle_post, name="detalle_post"),
    path("posts/<int:post_id>/editar/", views.editar_post, name="editar_post"),
    
]