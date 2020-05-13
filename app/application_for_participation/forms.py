from django import forms

from .models import SceneSlot

SOLO_OR_GROUP = (
    ("SL", "Сольное выступление"),
    ("GP", "Группа"),
)


class ApplicationForm(forms.Form):
    presentation_format = forms.ChoiceField(label='Формат выступления',
                                            choices=SOLO_OR_GROUP,
                                            required=True
                                            )
    name = forms.CharField(label='Название', max_length=128, required=True)
    text = forms.CharField(label='Сопроводительный текст', max_length=300, required=True)
    desired_scene_and_time_slot = forms.ModelChoiceField(label='Желаемая сцена и время', queryset=SceneSlot.objects.all(), empty_label=None, required=True)
    comment = forms.CharField(label='Коментарий', max_length=300, required=False)
