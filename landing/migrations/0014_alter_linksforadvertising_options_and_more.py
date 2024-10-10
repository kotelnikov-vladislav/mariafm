# Generated by Django 5.1.1 on 2024-10-10 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0013_linksforadvertising_linksforcontact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='linksforadvertising',
            options={'verbose_name': 'Секция "Подвал сайта": ссылка для рекламы', 'verbose_name_plural': 'Секция "Подвал сайта": ссылки для рекламы'},
        ),
        migrations.AlterModelOptions(
            name='linksforcontact',
            options={'verbose_name': 'Секция "Подвал сайта": ссылка для контактов', 'verbose_name_plural': 'Секция "Подвал сайта": ссылка для контактов'},
        ),
        migrations.AlterModelOptions(
            name='navlink',
            options={'verbose_name': 'Секция "Шапка сайта": ссылка навигации', 'verbose_name_plural': 'Секция "Шапка сайта": ссылки навигации'},
        ),
        migrations.AlterModelOptions(
            name='people',
            options={'ordering': ['order'], 'verbose_name': 'Секция "Команда": член команды', 'verbose_name_plural': 'Секция "Команда": члены команды'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['order'], 'verbose_name': 'Общие настройки: проект', 'verbose_name_plural': 'Общие настройки: проекты'},
        ),
        migrations.AlterModelOptions(
            name='seo',
            options={'verbose_name': 'Общие настройки: SEO', 'verbose_name_plural': 'Общие настройки: SEO'},
        ),
    ]
