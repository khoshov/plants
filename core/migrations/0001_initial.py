# Generated by Django 3.2.3 on 2021-05-30 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='название')),
                ('color', models.CharField(max_length=255, verbose_name='цвет')),
                ('size', models.PositiveSmallIntegerField(choices=[(0, 'Маленький'), (1, 'Средний'), (2, 'Большой')], verbose_name='размер')),
            ],
            options={
                'verbose_name': 'Растение',
                'verbose_name_plural': 'Растения',
            },
        ),
    ]
