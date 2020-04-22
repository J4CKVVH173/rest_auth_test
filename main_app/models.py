from django.db import models

# Create your models here.


class MainModel(models.Model):

    text = models.CharField(max_length=120)
    number = models.IntegerField()
