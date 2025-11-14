from django.urls import path

from .views import terciario_inicio, crear_alumno

urlpatterns = [
    path("", terciario_inicio),
    path("crear-alumno", crear_alumno)
]
