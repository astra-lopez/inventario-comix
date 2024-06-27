from django.db.models import fields
from rest_framework import serializers
from .models import Comic, Sale

class ComicSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comic
    fields = "__all__"


class SaleSerializer(serializers.ModelSerializer):
  comics = ComicSerializer(many=True, read_only=True)

  class Meta:
    model = Sale
    fields = ('id', 'user', 'comics', 'datetime')