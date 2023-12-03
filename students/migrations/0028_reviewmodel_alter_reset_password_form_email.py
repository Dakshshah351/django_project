# Generated by Django 4.2.3 on 2023-11-30 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0027_alter_usermodel_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='reviewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.EmailField(max_length=254)),
                ('project_title', models.CharField(max_length=100)),
                ('dev_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='reset_password_form',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
