from django.contrib import admin

from .models import Collection, Photo


class PhotoAdmin(admin.TabularInline):
    model = Photo
    readonly_fields = ('preview',)
    fields = (
        'preview',
        'file',
        'description'
    )


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'description',
        ('date_from', 'date_to')
    )
    inlines = [PhotoAdmin]
