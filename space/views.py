from django.shortcuts import redirect, render

from .models import spaceship

# Create your views here.


def index(request):

    space = spaceship.objects.all()

    return render(request, "index.html", {"space": space, "name": "aritimits"})


def about(request):
    return render(request, "about.html")


def projects(request):
    return render(request, "projects.html")


def blog(request):
    return render(request, "blog.html")


def contact(request):
    return render(request, "contact.html")
