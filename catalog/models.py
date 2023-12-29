from django.db import models

# Create your models here.
from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=100)
    singer = models.CharField(max_length=100)
    description = models.TextField()
    cover_image = models.ImageField(default="default.png", upload_to='covers/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    duration = models.DurationField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Song"
        verbose_name_plural = "Songs"


class Singer(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="First name")
    last_name = models.CharField(max_length=30, verbose_name="Last name")
    pseudonym = models.CharField(max_length=30, verbose_name="Pseudonym")
    bio = models.TextField(verbose_name="biography")
    photo = models.ImageField(verbose_name="Image", default="default.png", upload_to='albums/')
    slug = models.SlugField(unique=True, db_index=True, verbose_name="URL")

    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    def __str__(self):
        return f"{self.pk} - {self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Singer"
        verbose_name_plural = "Singers"


class Genre(models.Model):
    name = models.CharField(max_length=50)
    albums = models.ManyToManyField(Album)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
