from django.urls import path
from .views import delete_user, inicio, view_create_users, view_usuarios, create_usuario

urlpatterns = [
    path ('', inicio, name="inicio"),
    path('ver_usuarios', view_usuarios, name="usuarios"),
    path('create_users', view_create_users),
    path('new_usuario/', create_usuario, name = "create_usuario"),
    path('delete_user/<int:user_id>', delete_user, name="delete_user")
]
