from django.shortcuts import render, get_object_or_404

from .models import Collection


def home(request):
    return render(request, 'home.html', context={
        'collections': Collection.objects.order_by('date_from')
    })


def collection(request, slug):
    return render(request, 'collection.html', context={
        'collection': get_object_or_404(Collection, slug=slug)
    })


def carousel(request, slug):
    collection_obj = get_object_or_404(Collection, slug=slug)

    # We query this now to compare its count to start_carousel value
    collection_photos = collection_obj.photo_set.all()

    try:
        start_carousel = int(request.GET.get('start', '1'))
    except ValueError:
        start_carousel = 1
    else:
        if start_carousel > collection_photos.count():
            start_carousel = 1

    return render(request, 'carousel.html', context={
        'collection': collection_obj,
        'start_carousel': start_carousel,
        'collection_photos': collection_photos
    })
