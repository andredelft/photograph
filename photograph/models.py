from django.db import models
from autoslug import AutoSlugField
from cloudinary.models import CloudinaryField


class Collection(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    date_from = models.DateField()
    date_to = models.DateField(blank=True, null=True)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name


class Photo(models.Model):
    file = CloudinaryField('image')
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self):
        try:
            public_id = self.image.public_id
        except AttributeError:
            public_id = ''

        return f'Photo {self.name}:{public_id}'
