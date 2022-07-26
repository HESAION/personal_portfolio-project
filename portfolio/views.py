from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all()[:4]
    return render(request, 'portfolio/home.html', {'projects': projects})
