from django.db import models


# Create your models here.

class Our_brunches(models.Model):
    state = models.CharField(max_length=250,null=True)

class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone=models.CharField(max_length=100)
    message  = models.CharField(max_length=500)
    def __str__(self):
        return self.name

    

    
