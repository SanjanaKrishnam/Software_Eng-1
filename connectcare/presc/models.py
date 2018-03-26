from django.db import models

# Create your models here.
class Presc(models.Model):
    doctor = models.CharField(max_length=255)
