from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from . models import Playlist
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def playlist_list(request):
    playlists = Playlist.objects.all()

    context = {
        "playlists":playlists

    }

    return render(request, "playlists/playlist_list.html", context)


def playlist_details(request):
    playlists = Playlist.objects.all()

    context = {
        "playlists": playlists

    }

    return render(request, "playlists/playlist_details.html", context)

def playlist_edit(request):
    playlists = Playlist.objects.all()

    context = {
        "playlists":playlists

    }

    return render(request, "playlists/playlist_list.html", context)
