from djmoney.models.fields import MoneyField
from django.db import models



# Create your models here.

#=======================================================================
class Make(models.Model):
  make = models.CharField(max_length=30, null=False, blank=False)

  class Meta:
      ordering = ['make']

  def __str__(self):
        return self.make

#=======================================================================
class Model(models.Model):
  make = models.ForeignKey(Make, on_delete=models.CASCADE)
  model = models.CharField(max_length=50, null=False, blank=False)

  class Meta:
      ordering = ['model']

  def __str__(self):
        return (self.model)

#=======================================================================
class Body(models.Model):
  class Meta:
      verbose_name        = 'Body'
      verbose_name_plural = 'Bodies'
      ordering = ['body']

  body  = models.CharField(max_length=50, null=False, blank=False)
  
  def __str__(self):
        return self.body

#=======================================================================
class Picture(models.Model):
  picture = models.ImageField(upload_to='images/')
  default = models.BooleanField()

  def __str__(self):
        return self.picture.url

#=======================================================================
class Car(models.Model):

  class Fuel_Type(models.IntegerChoices):
    GASOLINE = 1
    DIESEL   = 2
    ELECTRIC = 3
    HYBRID   = 4
    
  class Transmition(models.IntegerChoices):
    AUTOMATIC = 1
    MANUAL    = 2
    

  make        = models.ForeignKey(Make, on_delete=models.CASCADE)
  model       = models.ForeignKey(Model, on_delete=models.CASCADE)
  year        = models.PositiveIntegerField(null=True, blank=True)
  color       = models.CharField(max_length=20, null=True, blank=True)
  body        = models.ForeignKey(Body, null=True, blank=True, on_delete=models.CASCADE, default=5)
  vin         = models.CharField(max_length=17, null=True, blank=True)  
  price       = MoneyField(max_digits=6, decimal_places=0, default_currency='USD', null=True, blank=True)
  fuel        = models.PositiveIntegerField(choices=Fuel_Type.choices, default=1)
  millage     = models.PositiveIntegerField(null=True, blank=True)
  transmition = models.PositiveIntegerField(null=True, blank=True, choices=Transmition.choices, default=1)
  pictures    = models.ForeignKey(Picture, null=True, blank=True, on_delete=models.CASCADE)
  description = models.TextField(null=True, blank=True)


  def __str__(self):
        return ("%s %s %s" % (self.year, self.make, self.model)).upper()



#=======================================================================