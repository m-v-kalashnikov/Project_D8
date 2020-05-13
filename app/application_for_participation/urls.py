from django.urls import path

from .views import application_view

app_name = 'application_for_participation'

urlpatterns = [
    path('view/', application_view, name="application"),
]
