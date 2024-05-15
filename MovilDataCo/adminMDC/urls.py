from django.urls import path
from .views import delete_user, file_upload, inicio, new_account, password_reset, processing_file, view_History, view_Shift, view_create_users, view_usuarios, create_usuario, help_password, what_choice

urlpatterns = [
    path('', inicio, name="inicio"),
    path('ayuda_contrasena', help_password, name="ayuda_contra"),
    path('contrasena', password_reset, name="contra_reset"),
    path('new_account', new_account, name="cuenta_nueva"),

    path('choice', what_choice, name="eleccion"),
    path('upload', file_upload, name="subida_archivos"),
    path('processing', processing_file, name="procesando_archivo"),
    path('view_Historia', view_History, name="Historia"),
    path('view_Tendencia', view_Shift, name="Tendencia"),

    path('ver_usuarios', view_usuarios, name="usuarios"),
    path('create_users', view_create_users),
    path('new_usuario/', create_usuario, name = "create_usuario"),
    path('delete_user/<int:user_id>', delete_user, name="delete_user")
]
