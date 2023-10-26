import typing

from rest_framework import serializers

from .song_serializer import SongSerializer
from ..models import Playlist


class PlaylistSerializer(serializers.ModelSerializer):

	songs = SongSerializer(many=True)

	class Meta:
		model = Playlist
		fields = ["id", "songs", "title", "cover"]
