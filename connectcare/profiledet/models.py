from django.db import models

# Create your models here.
USER_CHOICES = (('public','PUBLIC'),('patient','PATIENT'),('doctor','DOCTOR'),)

class USERMODEL(models.Model):
    type = models.CharField(max_length = 7, choices = USER_CHOICES,default='public')
