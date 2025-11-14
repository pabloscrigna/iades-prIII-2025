from django.shortcuts import render, HttpResponse

from .form import AlumnoForm


# Create your views here.
def terciario_inicio(request):
    return HttpResponse("En construccion")


def crear_alumno(request):

    if request.POST:
        print("Se envio a crear un alumno")

        return HttpResponse("En construccion")

    alumnos_form = AlumnoForm()
    return render(request, "crear_alumno.html", {"alumnos_form": alumnos_form})
