from django.shortcuts import render, redirect
from .models import Usuarios

# Create your views here.

def inicio(request):
    return render(request, 'MainInterface.html')

def view_usuarios(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'Users.html', {'users': usuarios})

def view_create_users(request):
    return render(request, 'CreateUsers.html')

def create_usuario(request):
    usuario = Usuarios(
        nombre = request.POST['nombre'],
        rol = request.POST['rol'],
        email = request.POST['email'],
        numero = request.POST['numero']
    )
    usuario.save()
    return redirect(view_usuarios)

def delete_user(request, user_id: int):
    user = Usuarios.objects.get(id=user_id)
    user.delete()
    return redirect(view_usuarios)
