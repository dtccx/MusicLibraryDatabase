from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import Artist
from .forms import ArtistForm

@login_required
def artist_list(request):

    artists = Artist.objects.all()

    query = request.GET.get("q")
    if query:
        artists = artists.filter(
            Q(name__icontains=query)
        )
        artists = artists.distinct()

    context = {
        "artists": artists,
    }
    # return HttpResponse("Here be I.")
    return render (request, "artists/artist_list.html", context)

@login_required
def artist_detail(request, id):
    artist = get_object_or_404(Artist, pk=id)

    context = {
        "state": None,
        "artist": artist,
    }

    # return HttpResponse("Here are the artists")
    return render (request, "artists/artist_detail.html", context)


def artist_edit(request, id):
    artist = get_object_or_404(Artist, pk=id)

    if request.method == "POST":
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            # artist=form.save()
            artist = form.save(commit=False)
            artist.save()
            form.save_m2m()

            messages.success(request, "Artist updated!")
            return redirect("artists:artist_detail", id=artist.pk)

    else:
        form = ArtistForm(instance=artist)

    context = {
        "form": form,
        "artist": artist,
    }

    return render(request, "artists/artist_edit.html", context)























