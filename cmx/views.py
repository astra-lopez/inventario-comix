from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UsuarioRegistro, ProductoForm, OrdenForm
from .models import Producto, Orden


@login_required
def index(request):
  ordenes = Orden.objects.all()
  usuarios = User.objects.all()[:2]
  productos = Producto.objects.all()[:2]
  usuarios_cantidad = len(User.objects.all())
  productos_cantidad = len(Producto.objects.all())
  ordenes_cantidad = len(Orden.objects.all())
  contexto = {
    "title": "Home",
    "ordenes": ordenes,
    "usuarios": usuarios,
    "productos": productos,
    "usuarios_cantidad": usuarios_cantidad,
    "productos_cantidad": productos_cantidad,
    "ordenes_cantidad": ordenes_cantidad,
  }

  return render(request, "index.html", contexto)


@login_required
def productos(request):
  productos = Producto.objects.all()
  if request.method == "POST":
    form = ProductoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("productos")
  else:
    form = ProductoForm()
  context = {"title": "Productos", "productos": productos, "form": form}
  return render(request, "productos.html", context)

@login_required
def ordenes(request):
  ordenes = Orden.objects.all()
  print([i for i in request])
  if request == "POST":
    form = OrdenForm(request.POST)
    if form.is_valid():
      instance = form.save(commit=False)
      instance.ordenada_por = request.user
      instance.save(commit=True)
      return redirect("ordenes")
  else:
    form = OrdenForm()
  context = {"title": "Ordenes", "ordenes": ordenes, "form": form}
  return render(request, "ordenes.html", context)

@login_required
def users(request):
  users = User.objects.all()
  context = {"title": "Usuarios", "users": users}
  return render(request, "usuarios.html", context)

@login_required
def user(request):
  context = {"perfil": "Perfil de usuario"}
  return render(request, "usuario.html", context)

def registro(request):
  if request.method == "POST":
    form = UsuarioRegistro(request.POST)
    if form.is_valid():
      form.save()
      return redirect("login")
  else:
    form = UsuarioRegistro()
  context = {"registro": "Registro", "form": form}
  return render(request, "registro.html", context)