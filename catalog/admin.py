from django.contrib import admin
from .models import Album, Song, Genre, Singer


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'singer', 'created_at')
    search_fields = ('title', 'singer')


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'duration')
    list_filter = ('album',)
    search_fields = ('title', 'album__title')


@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "pseudonym",)
    prepopulated_fields = {"slug": ("first_name", "last_name",)}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('albums',)
    search_fields = ('name',)
