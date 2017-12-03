from django import forms

from .models import Album

class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ("album_name",)
        model = Album
        fields = ("album_name")
        model = Album
        fields = ("collection_or_greatest_hits")
        model = Album
        fields = ("studio_or_live")
        model = Album
        fields = ("year_released")

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["album_name"].widget.attrs.update({
            "class":"form-control",

        self.fields["album_name"].widget.attrs.update({
            "class":"form-control",

        self.fields["collection_or_greatest_hits"].widget.attrs.update({
            "class":"form-control",

        self.fields["studio_or_live"].widget.attrs.update({
            "class":"form-control",

        self.fields"year_released"].widget.attrs.update({
            "class":"form-control",
        })
