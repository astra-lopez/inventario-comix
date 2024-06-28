from email.policy import default
from django.db import models
from django.contrib.auth.models import User

CATEGORIA = (
  ("Comics", "Comics"),
  ("Mercancía", "Mercancía"),
  ("Misc", "Misc"),
)

class UsuarioPerfil(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  rut = models.TextField(max_length=11)
  direccion_fisica = models.CharField(max_length=40)
  celular = models.CharField(max_length=12, null=True)

  def __str__(self) -> str:
    return self.user.username
  
class Producto(models.Model):
  nombre = models.CharField(max_length=100)
  categoria = models.CharField(max_length=10, choices=CATEGORIA)
  cantidad = models.PositiveIntegerField()
  descripcion = models.CharField(max_length=200)

  def __str__(self) -> str:
    return self.nombre
  
class Orden(models.Model):
  producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
  ordenada_por = models.ForeignKey(User, on_delete=models.CASCADE)
  cantidad_ordenada = models.PositiveIntegerField()
  fecha = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
    return f"{self.producto.nombre}, {self.cantidad_ordenada} unidad{'es' if self.candidad_ordenada else ''}"
