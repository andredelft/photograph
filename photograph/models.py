from django.db import models
from autoslug import AutoSlugField


class Collection(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    date_from = models.DateField()
    date_to = models.DateField(blank=True, null=True)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name


class Photo(models.Model):
    file = models.ImageField()
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
