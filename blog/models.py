from django.db import models

# Create your models here.

class cardAdd(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(max_length=255)
    image = models.ImageField(upload_to='image/')


class infoAdd(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(max_length=255)
    image = models.ImageField(upload_to='image/')
