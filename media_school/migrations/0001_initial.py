# Generated by Django 5.1.1 on 2024-10-16 17:31

import webpfield.fields
import webpfield.webp_storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MediaSchool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.CharField(max_length=500, verbose_name='Описание')),
                ('coverDesktop', webpfield.fields.WebPField(storage=webpfield.webp_storage.WebPStorage(), upload_to='', verbose_name='Изображение')),
                ('buttonLink', models.URLField(verbose_name='Ссылка для кнопки')),
                ('buttonCaption', models.CharField(max_length=20, verbose_name='Надпись в кнопке')),
            ],
            options={
                'verbose_name': 'Контент',
                'verbose_name_plural': 'Контент',
            },
        ),
    ]
