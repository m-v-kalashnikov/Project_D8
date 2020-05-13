from django.urls import path

from .views import home

app_name = 'viewing'

urlpatterns = [
    path('', home, name="home"),
]
