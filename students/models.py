from django.db import models
from distutils.command.upload import upload
from django.contrib.auth.models import AbstractUser
from django.db.models import Model
from django.utils import timezone

ROLL = (
    ('', 'Choose...'),
    (2, 'Leader'),
    (1, 'Developer')
)
# Create your models here.
class UserModel(AbstractUser):
    userProfile=models.ImageField(upload_to="userProfile")
    roll=models.IntegerField(choices=ROLL)
    technology=models.CharField(max_length=255,null=True,blank=True)
    Assigned_by = models.CharField(max_length=50,blank=True, null=True)


class RequirementModel(models.Model):
    id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    Client_name = models.CharField(max_length=255)
    project_title = models.CharField(max_length=255)
    project_Technology = models.CharField(max_length=255,blank=True, null=True)
    project_Description = models.TextField(max_length=255)
    start_date=models.DateField(default=timezone.now)
    end_date=models.DateField(blank=True, null=True)
    Client_email = models.EmailField(max_length=255)
    assigned_dev = models.CharField(max_length=255)
    DEVdeadline=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.Client_name

class pending_projects(models.Model):
    id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    project_title = models.CharField(max_length=255)
    Upload_File=models.FileField(upload_to="Upload_File")
    def __str__(self):
        return self.Upload_File
class adminPanel(models.Model):
   
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    password = models.CharField( max_length=255,verbose_name='password')
    email = models.EmailField(max_length=255)
   
    def __str__(self):
        return self.username

class reset_password_Form(models.Model):
    email = models.EmailField(max_length=100)
    def __str__(self):
        return self.email
class PasswordToken(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=6)  # Assuming OTPs are 6 characters long

    def __str__(self):
        return self.email  # You can customize this as needed
class reviewModel(models.Model):
    id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    description = models.TextField(max_length=255)
    project_title = models.CharField(max_length=100)  # Assuming OTPs are 6 characters long
    dev_id = models.CharField(max_length=100)
    def __str__(self):
        return self.email  # You can customize this as needed