from django.urls import path

from menu.apps import MenuConfig
from menu.views import IndexPageView

app_name = MenuConfig.name

urlpatterns = [
    path('', IndexPageView.as_view(), name='index')
]
