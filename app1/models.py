from django.db import models

# Create your models here.
class teacher(models.Model):
    cname=models.CharField(max_length=500)
class answer(models.Model):
    name=models.CharField(max_length=500)  
class trainerl(models.Model):
    tlog=models.CharField(max_length=50)  
class studentl(models.Model):
    slog=models.CharField(max_length=50)   