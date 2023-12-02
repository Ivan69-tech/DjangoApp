from django.db import models
import uuid
# Create your models here.

class Post(models.Model):
    
    
    title = models.CharField(max_length = 255)
    body = models.TextField()

    def __str__(self):
        return self.title

class Contact(models.Model):
    description = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photos/")
    
    def __str__(self):
           return self.description

class ExcelFile(models.Model):
    nom_excel = models.FileField(upload_to="file/")
        
    def __str__(self):
           return self.nom_excel


class Test(models.Model):
    test_id = models.AutoField(primary_key = True)
    nom = models.CharField(max_length=255)
        
    def __str__(self):
           return self.nom
    

