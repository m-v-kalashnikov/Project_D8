# Generated by Django 3.0.6 on 2020-05-10 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application_for_participation', '0004_auto_20200508_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='applications_condition',
            field=models.CharField(choices=[('PD', 'На рассмотрении'), ('CF', 'Принято'), ('RF', 'Отказано')], max_length=2, null=True, verbose_name='Состояние заявки'),
        ),
    ]
