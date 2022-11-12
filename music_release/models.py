from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import duration

from music.settings import AUTH_USER_MODEL


class Genre(models.Model):
    genre = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["genre"]

    def __str__(self):
        return f"{self.genre}"


class Artist(AbstractUser):
    pseudonym = models.CharField(max_length=255)

    class Meta:
        ordering = ["pseudonym"]

    def __str__(self):
        return self.pseudonym


class Album(models.Model):
    title = models.CharField(max_length=255)
    artists = models.ManyToManyField(to=AUTH_USER_MODEL, related_name="albums")
    length = models.DurationField()
    release_date = models.DateField()

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} ({self.release_date})"


class Song(models.Model):
    title = models.CharField(max_length=255)
    lyrics = models.TextField(blank=True)
    length = models.DurationField()
    genres = models.ManyToManyField(to=Genre, related_name="songs")
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs")

    def __str__(self):
        return self.title
