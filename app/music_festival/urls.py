from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import settings

urlpatterns = [
    path('hiden/admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('account_creation.urls', namespace="account_creation")),
    path('application/', include('application_for_participation.urls', namespace="application_for_participation")),
    path('voting/', include('voting_for_application.urls', namespace="voting_for_application")),
    path('', include('viewing.urls', namespace="viewing")),

]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
