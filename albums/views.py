from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from . models import Album
from django.http import HttpResponse


def album_list(request):
    albums = Album.objects.all()

    context = {
        "albums":albums

    }

    return render(request, "albums/album_list.html", context)


def album_details(request):
    albums = Album.objects.all()

    context = {
        "albums": albums

    }

    return render(request, "albums/album_details.html", context)

def album_edit(request):
    albums = Album.objects.all()

    context = {
        "albums":albums

    }

    return render(request, "albums/album_list.html", context)
