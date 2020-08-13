from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class food(models.Model):
    name = models.CharField(max_length=100)
    protein = models.FloatField()
    carbohydrate = models.FloatField()
    fat = models.FloatField()
    calorie = models.IntegerField()
    quantity = models.IntegerField() #1u,100g eg. 1 unit, 100 g
    unit = models.CharField(max_length=1) #u=unit,g=gram,m=ml
    maxIntake = models.IntegerField()
    img = models.ImageField(upload_to='foodPics')
    desc = models.CharField(max_length=500)
    bestFor = models.CharField(max_length=2, null=True) #P, F, C more protein,good fats, complex carbs(these are required for explore section)
    


class extendUser(models.Model):
    height = models.IntegerField()
    age = models.IntegerField()
    weight = models.IntegerField()
    sex = models.CharField(max_length=15)
    goal = models.CharField(max_length=15)
    activity = models.CharField(max_length=15)
    reqProtein = models.IntegerField()
    reqCarbs = models.IntegerField()
    reqFat = models.IntegerField()
    reqCalorie = models.IntegerField()
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    dietStatus = models.BooleanField(default=False)
    diet = models.CharField(default=" ",max_length=2000)
    macroStatus = models.CharField(max_length=200, default="Your Macronutrients not set currently. Calculate your macronutrients from the calculator given here.")
    dtStatus = models.CharField(max_length=200, default="Diet not set yet.")


    