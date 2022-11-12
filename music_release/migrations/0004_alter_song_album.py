# Generated by Django 4.1.3 on 2022-11-11 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("music_release", "0003_remove_album_songs_song_album"),
    ]

    operations = [
        migrations.AlterField(
            model_name="song",
            name="album",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="songs",
                to="music_release.album",
            ),
        ),
    ]
