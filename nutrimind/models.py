from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

class User(AbstractUser):
    pass

class PsychologicalCondition(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# UserProfile model that references the psychological condition
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.FloatField()

   
    psychological_condition = models.ForeignKey(PsychologicalCondition, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

# Recommendation model
class Recommendation(models.Model):
    meal_plan = models.TextField()
    yoga_exercises = models.TextField()
    psychological_condition = models.ForeignKey(PsychologicalCondition, on_delete=models.CASCADE)

    def __str__(self):
        return f"Recommendation for {self.psychological_condition.name}"
