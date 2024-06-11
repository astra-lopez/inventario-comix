from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
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