# Generated by Django 3.0.6 on 2020-05-08 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application_for_participation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='day',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Первый'), (2, 'Второй')], null=True, verbose_name='День'),
        ),
    ]
