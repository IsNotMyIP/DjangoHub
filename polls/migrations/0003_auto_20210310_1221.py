# Generated by Django 3.1.7 on 2021-03-10 11:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice_cdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='cDate',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='fecha publicada'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='fecha publicada'),
        ),
    ]
