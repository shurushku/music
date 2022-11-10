from django import forms
from django.forms import ModelForm

from .models import Genre, Album, Artist


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["genre"].widget.attrs.update({"class": "form-control"})
        self.fields["description"].widget.attrs.update({"class": "form-control"})


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ("title", "length", "release_date", "artists")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({"class": "form-control"})
        self.fields["artists"].widget.attrs.update({"class": "form-control"})
        self.fields["length"].widget.attrs.update({"class": "form-control"})
        self.fields["release_date"].widget.attrs.update({"class": "form-control"})


class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = ("pseudonym", "first_name", "last_name")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["pseudonym"].widget.attrs.update({"class": "form-control"})
        self.fields["first_name"].widget.attrs.update({"class": "form-control"})
        self.fields["last_name"].widget.attrs.update({"class": "form-control"})
