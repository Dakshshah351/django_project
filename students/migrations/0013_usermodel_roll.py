# Generated by Django 4.2.3 on 2023-10-07 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0012_adminpanel'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='roll',
            field=models.IntegerField(default=1, max_length=23),
            preserve_default=False,
        ),
    ]