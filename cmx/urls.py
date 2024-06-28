from django.urls import path
from . import views

urlpatterns = [
  path("dash/", views.index, name="dash"),
  path("productos/", views.productos, name="productos"),
  path("ordenes/", views.ordenes, name="ordenes"),
  path("usuarios/", views.users, name="usuarios"),
  path("usuario/", views.user,name="usuario"),
  path("registro/", views.registro, name="registro"),
]