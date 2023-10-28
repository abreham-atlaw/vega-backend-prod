import typing
from enum import Enum

from django.db import models

import uuid

from features.authentication.models import VegaUser


class Song(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	title = models.CharField(max_length=255)
	audio = models.URLField()
	cover = models.URLField()
	lyrics = models.TextField()
	create_datetime = models.DateTimeField(auto_now_add=True)
	duration = models.FloatField()
	user = models.ForeignKey(VegaUser, on_delete=models.SET_NULL, null=True, blank=True)


class Playlist(models.Model):

	title = models.CharField(max_length=255)
	cover = models.URLField(max_length=255)
	songs = models.ManyToManyField(Song, )
	create_datetime = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(VegaUser, on_delete=models.CASCADE)
