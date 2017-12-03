from django import forms

from .models import Artist
from core.forms import BootstrapFormMixin
from songs.models import Song

class ArtistForm(BootstrapFormMixin, forms.ModelForm):
  
    songs = forms.ModelMultipleChoiceField(
        queryset=Song.objects.all(), 
        required=False, 
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Artist
        fields = (
            "name",
            "songs",
        )

  