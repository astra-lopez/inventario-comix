from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Sum

class User(AbstractUser):
  rut = models.CharField(max_length=10)

  def __str__(self) -> str:
    return f"{self.first_name} {self.last_name}"

class Comic(models.Model):
  title = models.CharField(max_length=255)
  series = models.CharField(max_length=255)
  author = models.CharField(max_length=255)
  category = models.CharField(max_length=255)
  subcategory = models.CharField(max_length=255)
  year = models.PositiveSmallIntegerField()
  cost = models.PositiveIntegerField(default=0)

  def __str__(self) -> str:
    return self.name

class Stock(models.Model):
  comics = models.Man

  
class Sale(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  comics = models.ManyToManyField(Comic)
  datetime = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"${self.datetime} ${self.user}"
