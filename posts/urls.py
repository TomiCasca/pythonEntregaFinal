from django.urls import path

from posts import views

urlpatterns = [
    path("", views.Inicio.as_view(), name="inicio"),
    path("posts/", views.ListaPosteos.as_view(), name="lista_posts"),
    path("posts/crear/", views.CrearPosteo.as_view(), name="crear_post"),
    path("posts/<int:pk>/", views.DetallePosteo.as_view(), name="detalle_post"),
    path("posts/<int:pk>/editar/", views.EditarPosteo.as_view(), name="editar_post"),
    path("posts/<int:pk>/borrar/", views.BorrarPosteo.as_view(), name="borrar_post"),
]
