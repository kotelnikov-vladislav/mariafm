# Generated by Django 5.1.1 on 2024-10-06 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_projectssection_project_section'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='section',
        ),
        migrations.DeleteModel(
            name='ProjectsSection',
        ),
    ]