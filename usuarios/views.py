from django.shortcuts import render, redirect
from usuarios.forms import CrearUsuario, EditarPerfil
from django.contrib.auth.decorators import login_required
from usuarios.models import Perfil

def registro(request):
    if request.method == "POST":
        formulario = CrearUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('iniciar_sesion')
            
    else:
        formulario = CrearUsuario()
    
    return render(request, 'usuarios/registro.html', {'form': formulario}) 

@login_required
def perfil(request):
    perfil, _ = Perfil.objects.get_or_create(user=request.user)
    return render(request, 'usuarios/perfil.html', {"perfil": perfil})

@login_required
def editar_perfil(request):
    
    perfil, _ = Perfil.objects.get_or_create(user=request.user)
    
    if request.method == "POST":
        formulario = EditarPerfil(request.POST, request.FILES, instance=perfil)
        if formulario.is_valid():
            formulario.save()
            
            return redirect('perfil')
    else:
        formulario = EditarPerfil(instance=perfil)
        
    return render(request, 'usuarios/editar_perfil.html', {'form': formulario, 'perfil': perfil})