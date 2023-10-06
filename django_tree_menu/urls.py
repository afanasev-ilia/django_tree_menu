from django.contrib import admin
from django.urls import include, path

from menu.apps import MenuConfig

urlpatterns = [
    path('', include('menu.urls', namespace=MenuConfig.name)),
    path('admin/', admin.site.urls),
]
