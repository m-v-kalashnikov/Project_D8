from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db import models


class Account(models.Model):
    class MusicianOrSensor(models.TextChoices):
        MUSICIAN = 'MC', _('Музыкант')
        SENSOR = 'SS', _('Цензор')

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    name = models.CharField('Имя/Название группы', max_length=128, null=True)
    musician_or_sensor = models.CharField('Роль пользователя',
                                          max_length=2,
                                          choices=MusicianOrSensor.choices,
                                          null=True
                                          )
    verified = models.BooleanField('Верифицирован (поле Только для цензоров)', default=False, null=True)

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'

    def __str__(self):
        return self.user.username

    def is_musician(self):
        return self.musician_or_sensor == 'MC'

    def is_sensor(self):
        return self.musician_or_sensor == 'SS'
