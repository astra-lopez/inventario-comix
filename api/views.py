from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import Comic, Sale
from .serializers import ComicSerializer, SaleSerializer
@api_view(['GET'])
def ApiOverview(request):
  api_urls = {
    "comics": {
      'all_comics': '/comics/',
      'Search by Title': '/comics/?title=title_name',
      'Search by Series': '/comics/?series=series_name',
      'Search by Category': '/comics/?category=category_name',
      'Search by Subcategory': '/comics/?subcategory=subcategory_name',
      'Add': '/comics/create',
      'Update': '/comics/update/pk',
      'Delete': '/comics/pk/delete'
    },
    "sales": {
      'all_sales': '/sales/',
    }
  } 

  return Response(api_urls)


### CRUD ######################################################################

# Seguramente prodría refactorizar todo este código y utilizar herencia y 
# clases abstractas para evitar repetir tanto código -- ¡Qué mal!
 
## Create view ################################################################
# Comics
@api_view(['POST'])
def add_comics(request):
  comic = ComicSerializer(data=request.data)

  # Validar que no exista aún
  if Comic.objects.filter(**request.data).exists():
    raise serializers.ValidationError('This data already exists')

  if not comic.is_valid():
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  comic.save()
  return Response(comic.data)
  
# Sales
@api_view(['POST'])
def add_sales(request):
  sale = SaleSerializer(data=request.data)

  if Sale.objects.filter(**request.data).exists():
    raise serializers.ValidationError('This data already exists')
  
  if not sale.is_valid():
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  # comic_list = []
  # for c in sale['comics']:
  #   comic_list.append(get_object_or_404(Comic, id=c))

  # sale['comics'] = comic_list

  sale.save()
  return Response(sale.data)

## Read view ##################################################################
# Comics
@api_view(['GET'])
def view_comics(request):
  # Buscar paremetros en la URL
  comics = Comic.objects.filter(**request.query_params.dict())\
            if request.query_params\
            else Comic.objects.all()

  # Si no hay nada en comics, tirar error
  if not comics:
    return Response(status.HTTP_404_NOT_FOUND)

  serializer = ComicSerializer(comics, many=True)
  return Response(serializer.data)
  
# Sales
@api_view(['GET'])
def view_sales(request):
  sales = Sale.objects.filter(**request.query_params.dict())\
           if request.query_params\
           else Sale.objects.all() 
  
  if sales:
    return Response(status.HTTP_404_NOT_FOUND)

  serializer = SaleSerializer(sales, many=True)
  return Response(serializer.data)
  
## Update view ################################################################
# Comics
@api_view(['POST'])
def update_comics(request, pk):
  comic = Comic.objects.get(pk=pk)
  data = ComicSerializer(instance=comic, data=request.data)

  # Si los datos no son validos, tirar error
  if not data.is_valid():
    return Response(status=status.HTTP_404_NOT_FOUND)

  data.save()
  return Response(data.data)

# Sales
@api_view(['POST'])
def update_sales(request, pk):
  sale = Sale.objects.get(pk=pk)
  data = SaleSerializer(instance=sale, data=request.data)

  if not data.is_valid():
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  data.save()
  return Response(data.data)
  
## Delete view ################################################################
# Comics
@api_view(['DELETE'])
def delete_comics(request, pk):
  comic = get_object_or_404(Comic, pk=pk)
  comic.delete()
  return Response(status=status.HTTP_202_ACCEPTED)

# Sales
@api_view(['DELETE'])
def delete_sales(request, pk):
  sale = get_object_or_404(Sale, pk=pk)
  sale.delete()
  return Response(status=status.HTTP_202_ACCEPTED)

# Wow, that's a whole CRUD right there! We are almost done! [citation needed]

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Comic, Sale
from django.contrib.auth.models import User
from .serializers import (
    ComicSerializer,
    SaleSerializer,
)

# Create your views here.
class ComicViewSet(viewsets.ModelViewSet):
    queryset = Comic.objects.all()
    serializer_class = ComicSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
