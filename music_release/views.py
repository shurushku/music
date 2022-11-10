from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import GenreForm, AlbumForm, ArtistForm
from .models import Artist, Album, Genre, Song


def index(request):
    return render(request, "music_release/index.html")


# ArtistView
class ArtistListView(LoginRequiredMixin, generic.ListView):
    model = Artist


class ArtistDetailView(LoginRequiredMixin, generic.DetailView):
    model = Artist
    queryset = Artist.objects.all()


class ArtistCreateView(LoginRequiredMixin, generic.CreateView):
    model = Artist
    form_class = ArtistForm
    success_url = reverse_lazy("music_release:artist-list")


class ArtistUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Artist
    form_class = ArtistForm
    success_url = reverse_lazy("music_release:artist-list")


class ArtistDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Artist
    success_url = reverse_lazy("")


# AlbumView
class AlbumListView(LoginRequiredMixin, generic.ListView):
    model = Album


class AlbumDetailView(LoginRequiredMixin, generic.DetailView):
    model = Album


class AlbumCreateView(LoginRequiredMixin, generic.CreateView):
    model = Album
    form_class = AlbumForm
    success_url = reverse_lazy("music_release:album-list")


class AlbumUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Album
    form_class = AlbumForm
    success_url = reverse_lazy("music_release:album-list")


class AlbumDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Album
    success_url = reverse_lazy("music_release:album-list")


# GenreView
class GenreListView(LoginRequiredMixin, generic.ListView):
    model = Genre


class GenreDetailView(LoginRequiredMixin, generic.DetailView):
    model = Genre


class GenreCreateView(LoginRequiredMixin, generic.CreateView):
    model = Genre
    form_class = GenreForm
    success_url = reverse_lazy("music_release:genre-list")


class GenreUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Genre
    form_class = GenreForm
    success_url = reverse_lazy("music_release:genre-list")


class GenreDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Genre
    success_url = reverse_lazy("music_release:genre-list")


# SongView
class SongListView(LoginRequiredMixin, generic.ListView):
    model = Song


class SongDetailView(LoginRequiredMixin, generic.DetailView):
    model = Song


class SongCreateView(LoginRequiredMixin, generic.CreateView):
    model = Song
    fields = "__all__"
    success_url = reverse_lazy("music_release:song-list")


class SongUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Song
    fields = "__all__"
    success_url = reverse_lazy("music_release:song-list")


class SongDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Song
    success_url = reverse_lazy("music_release:song-list")
