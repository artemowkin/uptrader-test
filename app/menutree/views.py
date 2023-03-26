from django.shortcuts import render
from django.http.request import HttpRequest

from .models import Menu


def menus_list(request: HttpRequest):
    menus = Menu.objects.all()
    return render(request, 'menus.html', {'menus': menus})
