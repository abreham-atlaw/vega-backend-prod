
from rest_framework import serializers

from features.core.models import Song


class SongSerializer(serializers.ModelSerializer):

	class Meta:
		model = Song
		fields = ["id", "title", "audio", "cover", "lyrics", "create_datetime", "duration"]
