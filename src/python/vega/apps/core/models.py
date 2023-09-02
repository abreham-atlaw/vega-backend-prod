import typing
from enum import Enum

from django.db import models

import uuid


class QueryParams(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	genre = models.CharField(max_length=255, null=True)
	era = models.CharField(max_length=255, null=True)
	mood = models.CharField(max_length=255, null=True)

	@property
	def lyrics(self) -> 'typing.List[str]':
		return [lyrics.value for lyrics in Lyrics.objects.filter(query_params=self)]

	@property
	def instruments(self) -> 'typing.List[str]':
		return [instrument.value for instrument in Instrumental.objects.filter(query_params=self)]


class Lyrics(models.Model):
	value = models.CharField(max_length=255)
	query_params = models.ForeignKey(QueryParams, on_delete=models.CASCADE)


class Instrumental(models.Model):
	value = models.CharField(max_length=255)
	query_params = models.ForeignKey(QueryParams, on_delete=models.CASCADE)


class Song(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	title = models.CharField(max_length=255)
	audio = models.URLField()
	cover = models.URLField()
	lyrics = models.TextField()
	create_datetime = models.DateTimeField(auto_now_add=True)
	duration = models.FloatField(null=True)


class GenerationRequest(models.Model):

	class Status(Enum):

		none = 0
		instrumental = 1
		lyrics = 2
		vocal = 3
		mix = 4
		done = 5

	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	song = models.ForeignKey(Song, on_delete=models.CASCADE, null=True)
	status = models.IntegerField(
		choices=[
			(status.value, status.name)
			for status in [
				Status.none,
				Status.instrumental,
				Status.lyrics,
				Status.vocal,
				Status.mix,
				Status.done
			]
		],
		max_length=255,
		default=Status.none.value
	)

