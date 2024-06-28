from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .models import Producto, Orden

class UsuarioRegistro(UserCreationForm):
  email = forms.EmailField()

  class Meta:
   model = User 
   fields = [
     "username",
     "first_name",
     "last_name",
     "email",
     "password1",
     "password2",
   ]

class ProductoForm(forms.ModelForm):
  class Meta:
    model = Producto
    fields = ["nombre", "categoria", "cantidad", "descripcion"]

class OrdenForm(forms.ModelForm):
  class Meta:
    model = Orden
    fields = ["producto", "cantidad_ordenada"]