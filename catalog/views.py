import logging

from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from catalog.models import Album

logger = logging.getLogger('album_logger')


def index(request):
    logger.info("Start application")
    return render(request, "index.html")


def catalog_view(request):
    albums = Album.objects.defer(
        'song',
        'singer',
        'genre',
        'created_at',
        'updated_at'
    )
    context = {
        "albums": albums
    }
    return render(request, "albums.html", context=context)


def album_detail(request, album_slug):
    album = Album.objects.prefetch_related().get(slug=album_slug)
    genres = album.genre.all()
    singers = album.singers.all()
    context = {
        "album": album,
        "genres": genres,
        "singers": singers
    }
    return render(request, 'album.html', context=context)


def favourite_add(request, album_id):
    album = Album.objects.get(id=album_id)
    profile = request.user.profile_user
    if profile.favourites.filter(id=album_id).exists():
        profile.favourites.remove(album)
    else:
        profile.favourites.add(album)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def favourite_list(request):
    f_albums = request.user.profile_user.favourites.all()
    context = {
        "f_albums": f_albums
    }
    return render(request, 'favourites.html', context=context)


def search_result(request):
    query = request.GET.get('q')
    albums = Album.objects.filter(title__icontains=query)
    context = {
        "albums": albums
    }

    return render(request, "search_res.html", context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h3>Page not found</h3>")
