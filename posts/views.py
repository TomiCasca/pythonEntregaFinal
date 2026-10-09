from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.views.generic.base import TemplateView

from posts.forms import FormularioPosteo
from posts.models import Posteo


class Inicio(TemplateView):
    template_name = "posts/inicio.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["ultimos_posts"] = Posteo.objects.order_by("-fecha_publicacion", "-id")[:3]
        return contexto


class ListaPosteos(ListView):
    model = Posteo
    template_name = "posts/lista_posts.html"
    context_object_name = "posts"
    ordering = ["-fecha_publicacion", "-id"]


class DetallePosteo(DetailView):
    model = Posteo
    template_name = "posts/detalle_post.html"


class CrearPosteo(LoginRequiredMixin, CreateView):
    model = Posteo
    form_class = FormularioPosteo
    template_name = "posts/crear_post.html"
    success_url = reverse_lazy("lista_posts")


class EditarPosteo(LoginRequiredMixin, UpdateView):
    model = Posteo
    form_class = FormularioPosteo
    template_name = "posts/editar_post.html"
    success_url = reverse_lazy("lista_posts")


class BorrarPosteo(LoginRequiredMixin, DeleteView):
    model = Posteo
    template_name = "posts/borrar_post.html"
    success_url = reverse_lazy("lista_posts")
