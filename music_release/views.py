from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import (
    GenreForm,
    GenreSearchForm,
    AlbumForm,
    AlbumSearchForm,
    ArtistForm,
    ArtistSearchForm,
    SongForm,
)
from .models import Artist, Album, Genre, Song


@login_required
def index(request):
    num_artists = Artist.objects.count()
    num_albums = Album.objects.count()
    num_genres = Genre.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_artists": num_artists,
        "num_albums": num_albums,
        "num_genres": num_genres,
        "num_visits": num_visits + 1,
    }

    return render(request, "music_release/index.html", context=context)


# ArtistView
class ArtistListView(LoginRequiredMixin, generic.ListView):
    model = Artist
    queryset = Artist.objects.filter(is_staff=0)
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        pseudonym = self.request.GET.get("pseudonym", "")

        context = super(ArtistListView, self).get_context_data(**kwargs)
        context["search_form"] = ArtistSearchForm(initial={
            "pseudonym": pseudonym
        })

        return context

    def get_queryset(self):
        form = ArtistSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                pseudonym__icontains=form.cleaned_data["pseudonym"]
            )

        return self.queryset


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
    success_url = reverse_lazy("music_release:artist-list")


# AlbumView
class AlbumListView(LoginRequiredMixin, generic.ListView):
    model = Album
    queryset = Album.objects.all()
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        title = self.request.GET.get("title", "")

        context = super(AlbumListView, self).get_context_data(**kwargs)
        context["search_form"] = AlbumSearchForm(initial={
            "title": title
        })

        return context

    def get_queryset(self):
        form = AlbumSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                title__icontains=form.cleaned_data["title"]
            )

        return self.queryset


class AlbumDetailView(LoginRequiredMixin, generic.DetailView):
    model = Album


class AlbumCreateView(LoginRequiredMixin, generic.CreateView):
    model = Album
    form_class = AlbumForm
    success_url = reverse_lazy("music_release:album-list")


class AlbumUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Album
    form_class = AlbumForm

    def get_success_url(self):
        return reverse_lazy("music_release:album-detail", kwargs=self.kwargs)


class AlbumDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Album
    success_url = reverse_lazy("music_release:album-list")


# GenreView
class GenreListView(LoginRequiredMixin, generic.ListView):
    model = Genre
    queryset = Genre.objects.all()
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        genre = self.request.GET.get("genre", "")

        context = super(GenreListView, self).get_context_data(**kwargs)
        context["search_form"] = GenreSearchForm(initial={
            "genre": genre
        })

        return context

    def get_queryset(self):
        form = GenreSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                genre__icontains=form.cleaned_data["genre"]
            )

        return self.queryset


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
class SongDetailView(LoginRequiredMixin, generic.DetailView):
    model = Song


class SongCreateView(LoginRequiredMixin, generic.CreateView):
    model = Song
    form_class = SongForm

    def get_form_kwargs(self):
        kwargs = super(SongCreateView, self).get_form_kwargs()
        kwargs.update(self.kwargs)
        return kwargs

    def get_success_url(self):
        kwargs = {
            "pk": self.kwargs["album"]
        }
        return reverse_lazy("music_release:album-detail", kwargs=kwargs)


class SongUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Song
    form_class = SongForm

    def get_success_url(self):
        return reverse_lazy("music_release:song-detail", kwargs=self.kwargs)


class SongDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Song
    success_url = reverse_lazy("music_release:album-list")
