# Generated by Django 4.2.3 on 2023-09-18 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_delete_pending_projects_members_email_members_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='pending_projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255)),
                ('project_title', models.CharField(max_length=255)),
                ('Client_email', models.EmailField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='members',
            name='email',
            field=models.EmailField(max_length=255),
        ),
        migrations.AlterField(
            model_name='members',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='members',
            name='password',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='members',
            name='username',
            field=models.CharField(max_length=255),
        ),
    ]
