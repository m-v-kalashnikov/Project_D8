from django import forms


MUSICIAN_OR_SENSOR = (
    ("MC", "Музыкант/Группа"),
    ("SS", "Цензор"),
)


class AccountForm(forms.Form):
    name = forms.CharField(label='Имя/название группы:', max_length=128, required=True)
    musician_or_sensor = forms.ChoiceField(label='Тип аккаунта:', choices=MUSICIAN_OR_SENSOR, required=True)
