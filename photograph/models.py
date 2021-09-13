from autoslug import AutoSlugField
from cloudinary.models import CloudinaryField

from django.db import models
from django.utils.safestring import mark_safe


class Collection(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    date_from = models.DateField()
    date_to = models.DateField(blank=True, null=True)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name


class Photo(models.Model):
    file = CloudinaryField()
    description = models.TextField(blank=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def preview(self):
        return mark_safe(
            self.file.image(transformation=[
                {'height': 150, 'width': 150, 'crop': 'thumb', 'gravity': 'face'}
            ])
        )

    def __str__(self):
        try:
            return self.file.public_id
        except AttributeError:
            return 'Photo (ID unknown)'
