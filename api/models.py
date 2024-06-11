from django.db import models

class Comic(models.Model):
  title = models.CharField(max_length=255)
  series = models.CharField(max_length=255)
  author = models.CharField(max_length=255)
  category = models.CharField(max_length=255)
  subcategory = models.CharField(max_length=255)
  year = models.PositiveSmallIntegerField() # No, no nos vamos a pasar del año 32_767,
                                            # no lo pienses tanto

  def __str__(self) -> str:
    return self.name