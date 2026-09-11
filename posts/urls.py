from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("contacto/", views.contacto, name="contacto"),
    
    # vistas en formato funcion
    # path("posts/", views.lista_posts, name="lista_posts"),
    # path("posts/crear/", views.crear_post, name="crear_post"),
    # path("posts/<int:post_id>/", views.detalle_post, name="detalle_post"),
    # path("posts/<int:post_id>/editar/", views.editar_post, name="editar_post"),
    # path("posts/<int:post_id>/borrar/", views.borrar_post, name="borrar_post"),
    
    # CBV
    path("posts/", views.ListaPosteos.as_view(), name="lista_posts"),
    path("posts/crear/", views.CrearPosteo.as_view(), name="crear_post"),
    path("posts/<int:pk>/", views.DetallePosteo.as_view(), name="detalle_post"),
    path("posts/<int:pk>/editar/", views.EditarPosteo.as_view(), name="editar_post"),
    path("posts/<int:pk>/borrar/", views.BorrarPosteo.as_view(), name="borrar_post"),
    
]