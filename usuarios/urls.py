from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from usuarios import views

urlpatterns = [
    # login
    path('iniciar-sesion/', LoginView.as_view(template_name='usuarios/iniciar_sesion.html'), name='iniciar_sesion'),
    # logout
    path('cerrar-sesion/', LogoutView.as_view(), name='cerrar_sesion'),
    # registro
    path('registro/', views.registro, name='registrar'),
    # perfil
    path('perfil/', views.perfil, name='perfil'),
    # editar perfil
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
]
