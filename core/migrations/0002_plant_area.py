# Generated by Django 3.2.3 on 2021-05-30 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='area',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Место произростания'),
        ),
    ]
