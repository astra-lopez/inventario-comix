from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import Comic
from .serializer import ComicSerializer

@api_view(['GET'])
def ApiOverview(request):
  api_urls = {
    'all_comics': '/',
    'Search by Title': '/?title=title_name',
    'Search by Series': '/?series=series_name',
    'Search by Category': '/?category=category_name',
    'Search by Subcategory': '/?subcategory=subcategory_name',
    'Add': '/create',
    'Update': '/update/pk',
    'Delete': '/comic/pk/delete'
  }

  return Response(api_urls)

# Create view
@api_view(['POST'])
def add_comic(request):
  comic = ComicSerializer(data=request.data)

  # Validar que no exista aún
  if Comic.objects.filter(**request.data).exists():
    raise serializers.ValidationError('This data already exists')

  if comic.is_valid():
    comic.save()
    return Response(comic.data)
  else:
    return Response(status=status.HTTP_404_NOT_FOUND)

# Read view
@api_view(['GET'])
def view_comics(request):
  # Buscar paremetros en la URL
  if request.query_params:
    comics = Comic.objects.filter(**request.query_params.dict())
  else:
    comics = Comic.objects.all()

  # Si no hay nada en comics, tirar error
  if comics:
    serializer = ComicSerializer(comics, many=True)
    return Response(serializer.data)
  else:
    return Response(status.HTTP_404_NOT_FOUND)
  
# Update view
@api_view(['POST'])
def update_comics(request, pk):
  comic = Comic.objects.get(pk=pk)
  data = ComicSerializer(instance=comic, data=request.data)

  # Si los datos no son validos, tirar error
  if data.is_valid():
    data.save()
    return Response(data.data)
  else: 
    return Response(status=status.HTTP_404_NOT_FOUND)
  
# Delete view
@api_view(['DELETE'])
def delete_comics(request, pk):
  comic = get_object_or_404(Comic, pk=pk)
  comic.delete()
  return Response(status=status.HTTP_202_ACCEPTED)

# Wow, that's a whole CRUD right there! We are almost done! [citation needed]