from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    return render(request, "posts/inicio.html")

def lista_posts(request):
    
    posts = [
        {"id": 1, "titulo": "Mi primer post", "autor": "Micaela"},
        {"id": 2, "titulo": "Estoy aprendiendo Django", "autor": "Alan"},
        {"id": 3, "titulo": "Ya somos cracks en esto de programar", "autor": "Todo el curso"},
    ]
    contexto = {"posts": posts}
    
    return render(request, "posts/lista_posts.html", contexto)

def contacto(request):
    return HttpResponse("Página de contacto")

def detalle_post(request, post_id):
    return HttpResponse(f"Estás viendo el post número {post_id}")