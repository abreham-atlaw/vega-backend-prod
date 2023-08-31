from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from apps.core.models import Song
from apps.core.serializers.song_serializer import SongSerializer


class SongDetailView(APIView):

	def get(self, request: Request) -> Response:
		song = get_object_or_404(Song, id=request.query_params.get("id"))
		serializer = SongSerializer(instance=song)

		return Response(
			serializer.data
		)
