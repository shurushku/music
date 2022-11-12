from django.test import TestCase
from django.urls import reverse

ARTIST_LIST_URL = reverse("music_release:artist-list")
ALBUM_LIST_URL = reverse("music_release:album-list")
GENRE_LIST_URL = reverse("music_release:genre-list")


class PublicTests(TestCase):
    def test_genre_login_required(self):
        response = self.client.get(GENRE_LIST_URL)

        self.assertNotEqual(response.status_code, 200)

    def test_album_list_login_required(self):
        response = self.client.get(ALBUM_LIST_URL)

        self.assertNotEqual(response.status_code, 200)

    def test_artist_login_required(self):
        response = self.client.get(ARTIST_LIST_URL)

        self.assertNotEqual(response.status_code, 200)
