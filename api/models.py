from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

class Comic(models.Model):
  title = models.CharField(max_length=255)
  series = models.CharField(max_length=255)
  author = models.CharField(max_length=255)
  category = models.CharField(max_length=255)
  subcategory = models.CharField(max_length=255)
  year = models.PositiveSmallIntegerField() # No, no nos vamos a pasar del año 32_767,
                                            # no lo pienses tanto
  cost = models.PositiveIntegerField(default=0)

  def __str__(self) -> str:
    return self.name
  
class Sale(models.Model):
  datetime = models.DateTimeField(auto_now=True)
  # TODO: Investigar como funciona el User model
  #user = models.ForeignKey(User, on_delete=models.CASCADE)
  # FIXME: Crear una tabla de clientes y sacar el nombre de ahí
  customer_name = models.CharField(max_length=255)
  comics = models.ManyToManyField(Comic)

  @property
  def total_price(self):
    queryset = self.comics.all().aggregate(total_price=Sum('cost', default=0))
    return queryset["total_price"]
  
  class Meta: 
    ordering = ["datetime"]

  def __str__(self):
    return f"${self.datetime}: $${self.total}"