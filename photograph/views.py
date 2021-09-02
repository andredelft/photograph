from django.shortcuts import render, get_object_or_404

from .models import Collection


def home(request):
    return render(request, 'home.html', context={
        'collections': Collection.objects.all()
    })


def collection(request, slug):
    collection_obj = get_object_or_404(Collection, slug=slug)
    return render(request, 'collection.html', context={
        'collection': collection_obj
    })
