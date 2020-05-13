from django.shortcuts import render

from application_for_participation.models import SceneSlot, Application, Scene
from .models import Information


def home(request):
    scenes = Scene.objects.all()
    inform = Information.objects.all()
    context = {'inform': inform, 'scenes': scenes}
    return render(request, 'viewing/home.html', context)
