from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from features.core.models import Song
from features.core.serializers.song_serializer import SongSerializer


class SongDetailView(APIView):

	def get(self, request: Request) -> Response:
		song = get_object_or_404(Song, id=request.query_params.get("id"))
		serializer = SongSerializer(instance=song)

		return Response(
			serializer.data
		)


class RecentSongsView(APIView):

	def get(self, request: Request) -> Response:
		songs = list(Song.objects.all())[::-1]
		serializer = SongSerializer(instance=songs, many=True)
		return Response(
			serializer.data
		)
