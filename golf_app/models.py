from django.db import models
import datetime
# Create your models here.

NINE = 9
EIGHTEEN = 18
MINOR = 5
ADULT = 8
SENIOR = 7
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

class options(models.Model):

    occurance = models.ForeignKey(round, on_delete=models.CASCADE)
    phone = models.ForeignKey(round, on_delete=models.CASCADE)
    cart = models.IntegerField(maximum = 2, default = 0)
    golf_balls = models.IntegerField(default=0)
    club_rentals = models.IntegerField(default=0)
    

    
class round(models.Model):

    occurance = models.DateTimeField(default = datetime.datetime.now)
    phone = models.ForeignKey(golfer, on_delete=models.CASCADE)
    holes = models.IntegerField(max_length= 2, 
    choices=[NINE, EIGHTEEN], default = 9)
    mem = models.IntegerField(default = None)
    price = models.FloatField(default = 0.0)
   
    def cal_price(self):
      curr = 0.0

      if(self.holes == NINE):
        if self.golfer.age < 18:
          curr += 5
        elif self.golfer.age > 18 & self.golfer.age < 65:
          curr += 8
        elif self.golfer.age > 65:
          curr += 7

        if self.round.mem < 18:
          curr += 5
        elif self.round.mem > 18 & self.round.mem < 65:
          curr += 8
        elif self.round.mem > 65:
          curr += 7

        elif self.round.holes == 18:
          if self.golfer.age < 18:
           curr += 10
          elif self.golfer.age > 18 & self.golfer.age < 65:
           curr += 16
          elif self.golfer.age > 65:
           curr += 14

          if self.round.mem < 18:
            curr += 10
          elif self.round.mem > 18 & self.round.mem < 65:
            curr += 16
          elif self.round.mem > 65:
            curr += 14

        curr += self.golf_balls * GOLF_BALLS
        curr += self.cart * CARTP
        curr += self.club_rentals * CLUBS

        price = curr

    def __str__ (self):
        return "( " + self.occurance + " " + self.phone + " )" + self.holes + ", " + self.mem1 + ", " + self.mem2 + ", " + self.mem3 + ", "