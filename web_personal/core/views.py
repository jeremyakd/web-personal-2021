from django.shortcuts import render, HttpResponse


def home(request):
    title = '<h1>Mi primera vista de Django</h1>'
    content = ''
    for i in range(10):
        content += '<p> Yo soy un parrafo de for en el ciclo: ' + str(i+1) + '<p>'
    return HttpResponse((title + content))

# Request => Solicitud
# Response => Respuesta
