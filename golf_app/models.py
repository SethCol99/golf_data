from django.db import models
import datetime
# Create your models here.

NINE = 9
EIGHTEEN = 18
MINOR = 5.00
ADULT = 15
SENIOR = 10
CARTP = 15
GOLF_BALLS = 2
CLUBS = 7

class golfer(models.Model):

    fname = models.CharField(max_length= 10)
    lname = models.CharField(max_length= 15)
    phone = models.CharField(max_length= 13)
    age = models.IntegerField(max_length= 3)

    def __str__ (self):
        return "( " + self.fname + " " + self.lname + " )" + self.phone + ", " + self.age

class round(models.Model):

    occurance = models.DateTimeField(default = datetime.datetime.now)
    phone = models.ForeignKey(golfer, on_delete=models.CASCADE)
    holes = models.IntegerField(max_length= 2, 
    choices=[9, 18], default = 9)
    mem1 = models.IntegerField(default = None)
    mem2 = models.IntegerField(default = None)
    mem3 = models.IntegerField(default = None)
    price = models.FloatField(default = 0.0)
   
    def cal_price(self):
      curr = 0.0
    
      if self.round.holes == 9:
        curr += 9.0

      elif self.round.holes == 18:
        
    
      if self.round.mem1 < 18:


        price = curr

    def __str__ (self):
        return "( " + self.occurance + " " + self.phone + " )" + self.holes + ", " + 

class options(models.Model):
    cart = models.IntegerField(maximum = 2, default = 0)
    golf_balls = models.IntegerField(default=0)
    club_rentals = models.IntegerField(default=0)
    
    