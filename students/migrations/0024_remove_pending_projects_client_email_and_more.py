# Generated by Django 4.2.3 on 2023-11-21 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0023_alter_requirementmodel_project_technology_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pending_projects',
            name='Client_email',
        ),
        migrations.RemoveField(
            model_name='pending_projects',
            name='client_name',
        ),
    ]
