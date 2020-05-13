from django.db import models


class Information(models.Model):
    what = models.CharField('Название', max_length=300, null=True)
    where = models.CharField('Где', max_length=300, null=True)
    when = models.DateField('Когда', null=True)
    description = models.CharField('Описание', max_length=300, null=True)

    class Meta:
        verbose_name = 'Служебная инвормация'
        verbose_name_plural = 'Служебная инвормация'

    def __str__(self):
        return self.what
