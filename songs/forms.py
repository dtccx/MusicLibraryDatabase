from django import forms

from .models import Song
from core.forms import BootstrapFormMixin

class SongForm (BootstrapFormMixin, forms.ModelForm):

    class Meta:
        model = Song
        fields = (
            "name",
            "length",
            "artists",
            "video",
        )

  


