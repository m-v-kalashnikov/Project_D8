from django import forms

from application_for_participation.models import SceneSlot

CHOICES = [
    ('1', 'Я голозую за'),
    ('-1', 'Я голосую против'),
    ('0', 'Я воздержываюсь')
]


class VotingForm(forms.Form):
    decision = forms.ChoiceField(label='Голосовать', choices=CHOICES, widget=forms.RadioSelect, required=True)


class ConfirmingForm(forms.Form):
    scene_slot = forms.ModelChoiceField(label='Где и когда будет выступать', queryset=SceneSlot.objects.exclude(max_num_of_performers=0), empty_label=None, required=True)
    verdict = forms.BooleanField(label='Принять в программу', required=True)


class RefusingForm(forms.Form):
    verdict = forms.BooleanField(label='Отказать в участии', required=True)
