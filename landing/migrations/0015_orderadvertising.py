# Generated by Django 5.1.1 on 2024-10-10 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0014_alter_linksforadvertising_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderAdvertising',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=30, verbose_name='Текст ссылки')),
                ('url', models.CharField(verbose_name='URL-ссылки')),
            ],
            options={
                'verbose_name': 'Общие настройки: кнопка заказа рекламы',
                'verbose_name_plural': 'Общие настройки: кнопка заказа рекламы',
            },
        ),
    ]
