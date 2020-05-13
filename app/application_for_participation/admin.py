from django.contrib import admin

from .models import Application, Scene, TimeSlot, SceneSlot

admin.site.register(Application)

admin.site.register(Scene)

admin.site.register(TimeSlot)

admin.site.register(SceneSlot)
