from django.urls import path

from menu import views
from menu.apps import MenuConfig

app_name = MenuConfig.name

urlpatterns = [
    path('', views.index, name='index'),
]
