# Generated by Django 4.2.3 on 2023-10-24 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0021_requirementmodel_assigned_dev'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='technology',
            field=models.CharField(default='default', max_length=255),
            preserve_default=False,
        ),
    ]
