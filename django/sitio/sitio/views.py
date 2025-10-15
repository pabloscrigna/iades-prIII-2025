from django.http import HttpResponse


def saludo(request):
   return HttpResponse('IADES -- Programacion III')
