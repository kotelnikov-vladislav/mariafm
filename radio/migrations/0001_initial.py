# Generated by Django 5.1.1 on 2024-10-20 09:43

import django.db.models.deletion
import webpfield.fields
import webpfield.webp_storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Radio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(max_length=500, verbose_name='Описание')),
                ('cover_desktop', webpfield.fields.WebPField(storage=webpfield.webp_storage.WebPStorage(), upload_to='', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Контент',
                'verbose_name_plural': 'Контент',
            },
        ),
        migrations.CreateModel(
            name='RadioBadge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Заголовок')),
                ('caption', models.CharField(max_length=40, verbose_name='Подпись')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядковый номер отображения')),
                ('radio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='badges', to='radio.radio', verbose_name='Контент')),
            ],
            options={
                'verbose_name': 'Бейдж',
                'verbose_name_plural': 'Бейджы',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='RadioPlaque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=60, verbose_name='Текст')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядковый номер отображения')),
                ('radio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plaques', to='radio.radio', verbose_name='Контент')),
            ],
            options={
                'verbose_name': 'Плашка',
                'verbose_name_plural': 'Плашки',
                'ordering': ['order'],
            },
        ),
    ]
