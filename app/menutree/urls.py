from django.urls import path

from . import views


urlpatterns = [
    path('', views.menus_list, name='menus_list')
]