from django.http import HttpResponse
from django.template import Context, loader, Template

from datetime import datetime


def saludo(request):
    return HttpResponse("IADES -- Programacion III")


def mica(request):
    return HttpResponse("<h1>Hola Micaela!</h1>")


def fecha_hora_view(request):

    fecha_hora = datetime.now().strftime("%Y-%m-%d -- %H%M")

    return HttpResponse(fecha_hora)


def url_dinamica_view(request, year, apellido):

    print(f"Recibimos el año: {year} -- apellido: {apellido}")

    return HttpResponse(f"<h2>Año: {year}  -- Apellido: {apellido} </h2>")


def pablo_view(request):

    html_template_file = open(
        "/home/pablo/Documents/iades/2025/II Cuatrimestre/iades-prIII-2025/django/sitio/sitio/templates/template_1.html"
    )

    html_template = Template(html_template_file.read())

    html_template_file.close()

    context = Context()

    view_html = html_template.render(context)

    return HttpResponse(view_html)


def pablo_view_2(request):

    lista_nombres = ["Juan", "Jose", "Pedro"]
    lista_edades = [23, 45, 12]
    lista_dni = ["23456789", "4567432", "232422424"]

    alumno = {
        "nombre": "Pablo",
        "apellido": "Gonzalez",
        "dni": "12345678",
    }

    fecha_hora = datetime.now().strftime("%Y-%m-%d -- %H:%M")

    plantilla = loader.get_template("template_2.html")

    context = {"alumno": alumno, "nombres": lista_nombres, "edades": lista_edades, "dni": lista_dni, "fecha_hora": fecha_hora}

    return HttpResponse(plantilla.render(context, request))


def pablo_view_3(request, alumno_id):

    from sitio.data import alumnos

    alumno_r = None

    for alumno in alumnos:
        if alumno["id"] == alumno_id:
            alumno_r = alumno
            break

    plantilla = loader.get_template("template_3.html")

    context = {"alumno": alumno_r}

    return HttpResponse(plantilla.render(context, request))