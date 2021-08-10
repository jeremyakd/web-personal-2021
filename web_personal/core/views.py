from django.shortcuts import render
import json


def home(request):
    # Variables que se van a mandar al template mediante el contexto
    name = 'Jeremias'
    lastname = 'López'
    context = {
        'name' : name,
        'lastname' : lastname
    }
    return render(request, 'core/home.html', context=context)

def about(request):
	return render(request, 'core/about.html')

def portfolio(request):
    return render(request, 'core/portfolio.html')

def contact(request):
    return render(request, 'core/contact.html')
