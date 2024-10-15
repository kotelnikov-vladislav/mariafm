# Generated by Django 5.1.1 on 2024-10-13 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0015_orderadvertising'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='navlink',
            options={'ordering': ['order'], 'verbose_name': 'Секция "Шапка сайта": ссылка навигации', 'verbose_name_plural': 'Секция "Шапка сайта": ссылки навигации'},
        ),
        migrations.AddField(
            model_name='navlink',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Порядковый номер отображения'),
        ),
    ]