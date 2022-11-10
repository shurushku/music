from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models

from music.settings import AUTH_USER_MODEL


class Genre(models.Model):
    genre = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["genre"]

    def __str__(self):
        return f"{self.genre}"


class Song(models.Model):
    title = models.CharField(max_length=255)
    lyrics = models.TextField(blank=True)
    length = models.DurationField()
    genres = models.ManyToManyField(to=Genre)

    def __str__(self):
        return self.title


class Artist(AbstractUser):
    pseudonym = models.CharField(max_length=255)

    class Meta:
        ordering = ["pseudonym"]

    def __str__(self):
        return f"{self.pseudonym} ({self.first_name} {self.last_name})"


class Album(models.Model):
    title = models.CharField(max_length=255)
    artists = models.ManyToManyField(to=AUTH_USER_MODEL)
    length = models.DurationField()
    release_date = models.DateField()
    songs = models.ForeignKey(Song, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} ({self.release_date})"
