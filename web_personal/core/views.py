from django.shortcuts import render, HttpResponse

base_html = """
    <h1>Mi primera vista de Django</h1>
    <ul>
        <li><a href="/">Home</li>
        <li><a href="/about">Acerca de</li>
        <li><a href="/contact">Contacto</li>
        <li><a href="/portfolio">Portafolio</li>
    </ul>
"""

def home(request):
    content = ''
    for i in range(10):
        content += '<p> Yo soy un parrafo de for en el ciclo: ' + str(i+1) + '<p>'
    return HttpResponse((base_html + content))

# Request => Solicitud
# Response => Respuesta

def about(request):
    return HttpResponse(base_html +  '<h1>Acerca de</h1>')

def portfolio(request):
    return HttpResponse(base_html + '<h1>Portafolio</h1>')

def contact(request):
    return HttpResponse(base_html + '<h1>Contacto</h1>')
