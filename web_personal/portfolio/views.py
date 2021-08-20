from django.shortcuts import render
from .models import Project

def portfolio(request):
    todos_los_proyectos =  Project.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects': todos_los_proyectos})