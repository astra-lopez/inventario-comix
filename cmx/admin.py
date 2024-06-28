from django.contrib import admin
from cmx.models import Producto, Orden, UsuarioPerfil

admin.site.site_header = "Administrador de Inventario"

class ProductoAdmin(admin.ModelAdmin):
  model = Producto
  list_display = ("nombre", "categoria", "cantidad")
  list_filter = ["categoria"]
  search_fields = ["nombre"]

class OrdenAdmin(admin.ModelAdmin):
  model = Orden
  list_display = ("producto", "ordenada_por", "cantidad_ordenada", "fecha")
  list_filter = ["fecha"]
  search_fields = ["producto"]

class UsuarioPerfilAdmin(admin.ModelAdmin):
  model = UsuarioPerfil
  list_display = ("user", "rut", "direccion_fisica", "celular")
  list_filter = ["user"]
  search_fields = ["user", "rut"]

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Orden, OrdenAdmin)
admin.site.register(UsuarioPerfil, UsuarioPerfilAdmin)