from django.db import models

# Create your models here.
class login(models.Model):
    Mobile_Number = models.TextField(max_length=13)
    Latitude=models.FloatField()
    Longitude=models.FloatField()
class forest_department_login(models.Model):
    Name = models.TextField()
    Division = models.TextField()
    Designation = models.TextField()
    Email = models.EmailField()
class camera(models.Model):
    Video = models.TextField()
    Latitude=models.FloatField()
    Longitude=models.FloatField()
    Animal=models.TextField()
    Datetime=models.TextField()
class suggestions(models.Model):
    Name=models.TextField()
    Designation=models.TextField()
    Email=models.TextField()
    suggestions=models.TextField()
class report_intrusion(models.Model):
    Animal=models.TextField()
    Location=models.TextField()
    Date_and_Time=models.TextField()
class add_camera_Location(models.Model):
      Video=models.TextField()
      latitude=models.FloatField()
      longitude=models.FloatField()
      


