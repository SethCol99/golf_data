from django.db import models
import datetime
# Create your models here.

NINE = 9
EIGHTEEN = 18

class golfer(models.Model):

    fname = models.CharField(max_length= 10)
    lname = models.CharField(max_length= 15)
    phone = models.CharField(max_length= 13)
    