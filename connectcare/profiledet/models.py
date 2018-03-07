from django.db import models

# Create your models here.
USER_CHOICES = (('Public','PUBLIC'),('Patient','PATIENT'),('Doctor','DOCTOR'),)
BG = (('AB+','AB+'),('AB-','AB-'),('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('O+','O+'),('O-','O-'))

class USERMODEL(models.Model):
    type = models.CharField(max_length = 7, choices = USER_CHOICES,default='public')
    name = models.CharField(max_length = 255,null=True)
    aname = models.CharField(max_length = 255,null=True)
    phno = models.CharField(max_length = 10,null=True)
    dob  = models.DateField(max_length = 8,null=True)
    bg = models.CharField(max_length = 5,choices = BG,default = 'o+',null=True)
    qual = models.CharField(max_length = 255,blank=True,null=True)
    field = models.CharField(max_length = 255,blank= True,null = True)

class Extra(models.Model):
    qu = models.CharField(max_length = 255,null = True)
    fi = models.CharField(max_length = 255,null = True)
