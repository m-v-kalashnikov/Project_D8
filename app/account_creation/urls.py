from django.urls import path

from .views import account_view

app_name = 'account_creation'

urlpatterns = [
    path('profile/', account_view, name="account_profile"),
]
