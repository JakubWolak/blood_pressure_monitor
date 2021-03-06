# Generated by Django 3.0.8 on 2020-07-07 10:37

from django.db import migrations, models
import measurements.validators


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0002_auto_20200706_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='diastolic_pressure',
            field=models.SmallIntegerField(default=80, validators=[measurements.validators.max_diastolic_pressure, measurements.validators.min_diastolic_pressure], verbose_name='Ciśnienie rozkurczowe'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='pulse',
            field=models.SmallIntegerField(default=60, validators=[measurements.validators.max_pulse, measurements.validators.min_pulse], verbose_name='Tętno'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='systolic_pressure',
            field=models.SmallIntegerField(default=120, validators=[measurements.validators.max_systolic_pressure, measurements.validators.min_systolic_pressure], verbose_name='Ciśnienie skurczowe'),
        ),
    ]
