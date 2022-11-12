from django.urls import path

from .views import (
    index,
    ArtistListView,
    ArtistDetailView,
    ArtistCreateView,
    ArtistUpdateView,
    ArtistDeleteView,
    AlbumListView,
    AlbumDetailView,
    AlbumCreateView,
    AlbumUpdateView,
    AlbumDeleteView,
    GenreListView,
    GenreDetailView,
    GenreCreateView,
    GenreUpdateView,
    GenreDeleteView,
    SongDetailView,
    SongCreateView,
    SongUpdateView,
    SongDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("artists/", ArtistListView.as_view(), name="artist-list"),
    path("artists/<int:pk>/", ArtistDetailView.as_view(), name="artist-detail"),
    path("artists/create/", ArtistCreateView.as_view(), name="artist-create"),
    path("artists/<int:pk>/update/", ArtistUpdateView.as_view(), name="artist-update"),
    path("artists/<int:pk>/delete/", ArtistDeleteView.as_view(), name="artist-delete"),

    path("albums/", AlbumListView.as_view(), name="album-list"),
    path("albums/<int:pk>/", AlbumDetailView.as_view(), name="album-detail"),
    path("albums/create/", AlbumCreateView.as_view(), name="album-create"),
    path("albums/<int:pk>/update/", AlbumUpdateView.as_view(), name="album-update"),
    path("albums/<int:pk>/delete/", AlbumDeleteView.as_view(), name="album-delete"),

    path("genres/", GenreListView.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetailView.as_view(), name="genre-detail"),
    path("genres/create/", GenreCreateView.as_view(), name="genre-create"),
    path("genres/<int:pk>/update/", GenreUpdateView.as_view(), name="genre-update"),
    path("genres/<int:pk>/delete/", GenreDeleteView.as_view(), name="genre-delete"),

    path("songs/<int:pk>/", SongDetailView.as_view(), name="song-detail"),
    path("songs/create/<int:album>/", SongCreateView.as_view(), name="song-create"),
    path("songs/<int:pk>/update/", SongUpdateView.as_view(), name="song-update"),
    path("songs/<int:pk>/delete/", SongDeleteView.as_view(), name="song-delete"),
]

app_name = "music_release"
