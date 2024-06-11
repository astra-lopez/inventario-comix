from django.db.models import fields
from rest_framework import serializers
from .models import Comic

class ComicSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comic
    fields = ('title', 'series', 'author', 'category', 'subcategory', 'year')