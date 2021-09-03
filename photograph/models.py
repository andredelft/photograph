from django.db import models
from autoslug import AutoSlugField


class Collection(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True)
    date = models.DateField()
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name


class Photo(models.Model):
    name = models.CharField(max_length=50, unique=True)
    file = models.ImageField()
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
