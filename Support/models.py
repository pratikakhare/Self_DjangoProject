from django.db import models

# Create your models here.
class SupportDesk(models.Model):
    support_name = models.CharField(max_length=50)
    support_email = models.EmailField()
    support_date = models.DateField()
    support_time = models.TimeField()