import json
from django.shortcuts import render, redirect
from .models import Abonados, Ingresos, Trafico, Usuarios
from django.db import models

# Create your views here.

def inicio(request):
    return render(request, 'index.html')

def help_password(request):
    return render(request, 'HelpPassword.html')

def password_reset(request):
    return render(request, 'PasswordReset.html')

def new_account(request):
    return render(request, 'RegisterInterface.html')


def what_choice(request):
    return render(request, 'Choice.html')

def file_upload(request):
    return render(request, 'FileUpload.html')

def processing_file(request):
    return render(request, 'Processing.html')

def view_History(request):
    abonados = Abonados.objects.all()
    trafico = Trafico.objects.all()
    ingresos = Ingresos.objects.all()
    return render(request, 'History.html', {
        "abonados": abonados,
        "abonados_data": json.dumps(list(abonados.values())),
        "trafico_data": json.dumps(list(trafico.values())),
        "ingresos_data": json.dumps(list(ingresos.values())),
    })

def view_Shift(request):
    abonados = Abonados.objects.all()
    return render(request, 'Shift.html',{
        "abonados_data": json.dumps(list(abonados.values())),
    })


def view_usuarios(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'Users.html', {
        'users': usuarios,
        "users_data": json.dumps(list(usuarios.values()))
    })

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
