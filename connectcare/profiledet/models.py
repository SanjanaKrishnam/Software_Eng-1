from django.db import models

# Create your models here.
USER_CHOICES = (('public','PUBLIC'),('patient','PATIENT'),('doctor','DOCTOR'),)
BG = (('ab+','AB+'),('ab-','AB-'),('a+','A+'),('a-','A-'),('b+','B+'),('b-','B-'),('o+','O+'),('o-','O-'))
class USERMODEL(models.Model):
    type = models.CharField(max_length = 7, choices = USER_CHOICES,default='public')
    name = models.CharField(max_length = 255,blank = True,null = True)
    aname = models.CharField(max_length = 255,blank = True,null = True)
    phno = models.CharField(max_length = 10,blank = True,null = True)
    dob  = models.DateField(max_length = 8,blank = True,null=True)
    bg = models.CharField(max_length = 5,choices = BG,default = 'o+',null=True)
    qual = models.CharField(max_length = 255,blank=True,null = True)
    field = models.CharField(max_length = 255,blank= True,null = True)
