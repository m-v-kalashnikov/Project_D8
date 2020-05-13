from django import template

from application_for_participation.models import Application

register = template.Library()


@register.filter
def apps(scene):
    application = Application.objects.filter(applications_condition='CF')
    return application.filter(desired_scene_and_time_slot__scene=scene).order_by('rating')
