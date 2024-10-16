# Generated by Django 5.1.1 on 2024-10-16 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footer', '0002_alter_linksforadvertising_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterCaption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.TextField(max_length=250, verbose_name='Название ссылки')),
            ],
            options={
                'verbose_name': 'Подпись',
                'verbose_name_plural': 'Подпись',
            },
        ),
    ]