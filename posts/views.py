from django.http import HttpResponse
from django.shortcuts import render, redirect
from posts.models import Posteo
from posts.forms import FormularioCrearPosteo, FormularioEditarPosteo
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    return render(request, "posts/inicio.html")

def lista_posts(request):
    
    # posts = [
    #     {"id": 1, "titulo": "Mi primer post", "autor": "Micaela"},
    #     {"id": 2, "titulo": "Estoy aprendiendo Django", "autor": "Alan"},
    #     {"id": 3, "titulo": "Ya somos cracks en esto de programar", "autor": "Todo el curso"},
    # ]
    
    posts = Posteo.objects.all()
    
    contexto = {"posts": posts}
    
    return render(request, "posts/lista_posts.html", contexto)

def contacto(request):
    return HttpResponse("Página de contacto")

def detalle_post(request, post_id):
    
    posteo = Posteo.objects.get(id=post_id)
    
    return render(request, 'posts/detalle_post.html', {'post': posteo})

@login_required
def crear_post(request):

    # print(request.GET)
    # print(request.POST)

    if request.method == 'POST':
        
        formulario = FormularioCrearPosteo(request.POST, request.FILES)
        # print(request.POST)
        # print(request.FILES)
        if formulario.is_valid():
            # v1
            # info = formulario.cleaned_data
            # posteo = Posteo(titulo=info.get('titulo'), autor=info.get('autor'), contenido=info.get('contenido'))
            # posteo.save()
            
            # v2
            formulario.save()
            
            return redirect('lista_posts')
          
    else:
        formulario = FormularioCrearPosteo()
        
    return render(request, 'posts/crear_post.html', {'formulario': formulario})

def editar_post(request, post_id):
    
    posteo = Posteo.objects.get(id=post_id)
    
    if request.method == "POST":
        formulario = FormularioEditarPosteo(request.POST, request.FILES, instance=posteo)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_posts')
    else:
        formulario = FormularioEditarPosteo(instance=posteo)
        
    return render(request, 'posts/editar_post.html', {'formulario': formulario})

def borrar_post(request, post_id):
    
    posteo = Posteo.objects.get(id=post_id)
    posteo.delete()
    
    return redirect('lista_posts')


class CrearPosteo(CreateView):
    model = Posteo
    template_name = "posts/CBV/crear_post.html"
    success_url = reverse_lazy('lista_posts')
    fields = "__all__"

class ListaPosteos(ListView):
    model = Posteo
    template_name = "posts/CBV/lista_posts.html"
    context_object_name = 'posts'

class DetallePosteo(DetailView):
    model = Posteo
    template_name = "posts/CBV/detalle_post.html"

class EditarPosteo(LoginRequiredMixin, UpdateView):
    model = Posteo
    template_name = "posts/CBV/editar_post.html"
    success_url = reverse_lazy('lista_posts')
    # fields = "__all__"
    form_class = FormularioEditarPosteo

class BorrarPosteo(LoginRequiredMixin, DeleteView):
    model = Posteo
    template_name = "posts/CBV/borrar_post.html"
    success_url = reverse_lazy('lista_posts')
