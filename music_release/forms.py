from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import Genre, Album, Artist, Song


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["genre"].widget.attrs.update({"class": "form-control"})
        self.fields["description"].widget.attrs.update({"class": "form-control"})


class GenreSearchForm(forms.Form):
    genre = forms.CharField(
        max_length=255,
        required=True,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Search by genre",
            "type": "search",
            "class": "form-control form-input",
        })
    )


class AlbumForm(ModelForm):
    artists = forms.ModelMultipleChoiceField(
        queryset=Artist.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Album
        fields = ("title", "length", "release_date", "artists")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({"class": "form-control"})
        self.fields["length"].widget.attrs.update({"class": "form-control"})
        self.fields["release_date"].widget.attrs.update({"class": "form-control"})


class AlbumSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=True,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Search by album",
            "type": "search",
            "class": "form-control form-input",
        })
    )


class ArtistForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Artist
        fields = UserCreationForm.Meta.fields + (
            "pseudonym",
            "first_name",
            "last_name",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class": "form-control"})
        self.fields["pseudonym"].widget.attrs.update({"class": "form-control"})
        self.fields["first_name"].widget.attrs.update({"class": "form-control"})
        self.fields["last_name"].widget.attrs.update({"class": "form-control"})
        self.fields["password1"].widget.attrs.update({"class": "form-control"})
        self.fields["password2"].widget.attrs.update({"class": "form-control"})


class ArtistSearchForm(forms.Form):
    pseudonym = forms.CharField(
        max_length=255,
        required=True,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Search by pseudonym",
            "type": "search",
            "class": "form-control form-input",
        })
    )


class SongForm(ModelForm):
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Song
        fields = ("title", "lyrics", "length", "genres", "album")

    def __init__(self, album=None, *args, **kwargs):
        if album:
            kwargs.update(initial={
                'album': Album.objects.get(pk=album)
            })
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({"class": "form-control"})
        self.fields["lyrics"].widget.attrs.update({"class": "form-control"})
        self.fields["length"].widget.attrs.update({"class": "form-control"})
        self.fields["album"].widget.attrs.update({"style": "display: None"})
        self.fields["album"].label = ""

