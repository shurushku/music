from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Genre, Song, Album, Artist

admin.site.register(Genre)
admin.site.register(Song)
admin.site.register(Album)


@admin.register(Artist)
class DriverAdmin(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "pseudonym",
                    )
                },
            ),
        )
    )
