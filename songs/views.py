from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Count, Q

from .models import Song
from artists.models import Artist
from .forms import SongForm


def song_list(request):
    songs = Song.objects.all()

    query = request.GET.get("q")
    if query:
        # artists = Artist.objects.filter(name__icontains=query)
        songs = songs.filter(
            Q(name__icontains=query) 
            # Q(artists__in=artists)
        )
        songs = songs.distinct()

    context = {
        "songs": songs,
    }
    # return HttpResponse("Yup yup yup yup.")
    return render(request, "songs/song_list.html", context)

def song_detail(request, id):
    song = get_object_or_404(Song, pk=id)

    context = {
        "song": song,
    }

    # return HttpResponse("song details!")
    return render(request, "songs/song_detail.html", context)


def song_new(request):
    if request.method == "POST":
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save()
            messages.success(request, "Song added!")
            return redirect("songs/song_edit.html", id=song.pk)
    else:
        form = SongForm()

    context = {
        "form":form,
    }

    return render(request, "songs/song_edit.html", context)

def song_edit (request, id):
    song = get_object_or_404(Song, pk=id)

    if request.method == "POST":
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            song=form.save()
            messages.success(request, "Song updated!")
            return redirect("songs:song_detail", id=song.pk)

    else: 
        form = SongForm(instance=song)

    context = {
        "form": form, 
        "song": song,
    }

    return render(request, "songs/song_edit.html", context)























