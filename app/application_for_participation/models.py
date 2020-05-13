from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from typing import Iterable


class ListField(models.TextField):
    """
    A custom Django field to represent lists as comma separated strings
    """

    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', ',')
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs['token'] = self.token
        return name, path, args, kwargs

    def to_python(self, value):

        class SubList(list):
            def __init__(self, token, *args):
                self.token = token
                super().__init__(*args)

            def __str__(self):
                return self.token.join(self)

        if isinstance(value, list):
            return value
        if value is None:
            return SubList(self.token)
        return SubList(self.token, value.split(self.token))

    def from_db_value(self, value, expression, connection):
        return self.to_python(value)

    def get_prep_value(self, value):
        if not value:
            return
        assert(isinstance(value, Iterable))
        return self.token.join(value)

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)


class Application(models.Model):
    class SoloOrGroup(models.TextChoices):
        SOLO = 'SL', _('Сольное выступление')
        GROUP = 'GP', _('Группа')

    class Condition(models.TextChoices):
        PENDING = 'PD', _('На рассмотрении')
        CONFIRMED = 'CF', _('Принято')
        REFUSED = 'RF', _('Отказано')

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='application')
    name = models.CharField('Название', max_length=128, null=True)
    text = models.CharField('Текст', max_length=300, null=True)
    presentation_format = models.CharField('Формат выступления',
                                           max_length=2,
                                           choices=SoloOrGroup.choices,
                                           null=True
                                           )
    desired_scene_and_time_slot = models.ForeignKey('SceneSlot', on_delete=models.SET_NULL, null=True, related_name='application')
    comment = models.CharField('Коментарий', max_length=300, null=True)
    applications_condition = models.CharField('Состояние заявки',
                                              max_length=2,
                                              choices=Condition.choices,
                                              null=True
                                              )
    rating = models.SmallIntegerField("Рейтинг", default=0, null=True)
    voted_sensors = ListField(null=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.name

    def can_be_voted(self):
        if self.rating >= 3:
            return True
        elif self.rating <= (-5):
            return True
        else:
            return False


class Scene(models.Model):
    name = models.CharField('Название', max_length=128, null=True)
    description = models.CharField('Описание', max_length=300, null=True)

    class Meta:
        verbose_name = 'Сцена'
        verbose_name_plural = 'Сцены'

    def __str__(self):
        return self.name


class TimeSlot(models.Model):
    class Time(models.TextChoices):
        DAY = 'DY', _('День')
        NIGHT = 'NT', _('Вечер')
        LATE_NIGHT = 'LN', _('Поздний вечер')

    class Day(models.IntegerChoices):
        FIRST = 1, _('Первый')
        SECOND = 2, _('Второй')

    day = models.PositiveSmallIntegerField('День',
                                           choices=Day.choices,
                                           null=True
                                           )
    time = models.CharField('Время',
                            max_length=2,
                            choices=Time.choices,
                            null=True
                            )

    class Meta:
        verbose_name = 'Временной слот'
        verbose_name_plural = 'Временные слоты'

    def __str__(self):
        return '{} - {}'.format(self.get_day_display(), self.get_time_display())


class SceneSlot(models.Model):
    scene = models.ForeignKey('Scene', on_delete=models.SET_NULL, null=True, related_name='scene_slot')
    time_slot = models.ForeignKey('TimeSlot', on_delete=models.SET_NULL, null=True, related_name='scene_slot')
    max_num_of_performers = models.PositiveSmallIntegerField('Максимальное число выступающих', null=True)

    class Meta:
        verbose_name = 'Сценослот'
        verbose_name_plural = 'Сценослоты'

    def __str__(self):
        return 'Сцена {} - {}/{}'.format(self.scene.name, self.time_slot.get_day_display(), self.time_slot.get_time_display())
