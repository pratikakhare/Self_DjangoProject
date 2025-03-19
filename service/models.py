from django.db import models

# Create your models here.

class help(models.Model):
    help_id = models.CharField(max_length=50)
    help_title = models.CharField(max_length=50)
    help_des = models.TextField()
    
    
class Card(models.Model):
    card_id = models.CharField(max_length=50)
    card_title = models.CharField(max_length=50)
    card_des = models.TextField()