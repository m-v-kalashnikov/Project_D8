from django.urls import path
from .views import voting_list, voting_detail

app_name = 'voting_for_application'

urlpatterns = [
    path('list/', voting_list, name="voting_list"),
    path('detail/<str:user>/', voting_detail, name="voting_detail"),
]
