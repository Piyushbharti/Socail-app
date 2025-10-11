from django.db import models

# Create your models here.
class coustomerUser(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

class loginToken(models.Model):
    user = models.CharField(max_length=100)
    token = models.TextField()
    created = models.DateTimeField(auto_now_add=True)