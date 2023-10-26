import typing

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from features.core.models import Playlist, Song
from features.core.serializers import PlaylistSerializer


class CreatePlaylistView(APIView):

	permission_classes = [IsAuthenticated]

	def post(self, request: Request) -> Response:

		playlist: Playlist = Playlist.objects.create(
			user=request.user,
			title=request.data.get("title")
		)

		serializer = PlaylistSerializer(instance=playlist)

		return Response(
			serializer.data,
			status=201
		)


class PlaylistDetailView(APIView):

	permission_classes = [IsAuthenticated]

	def get(self, request: Request) -> Response:

		playlist = get_object_or_404(Playlist, pk=request.query_params.get("id"))
		serializer = PlaylistSerializer(instance=playlist)
		return Response(
			serializer.data,
		)


class PlaylistListView(APIView):

	permission_classes = [IsAuthenticated]

	def get(self, request: Request) -> Response:

		playlists = Playlist.objects.filter(user=request.user)
		serializer = PlaylistSerializer(instance=playlists, many=True)
		return Response(
			serializer.data
		)


class AddToPlaylistView(APIView):

	permission_classes = [IsAuthenticated]

	def post(self, request: Request) -> Response:
		song_id, playlist_id = request.data.get("song_id"), request.data.get("playlist_id")
		if song_id is None:
			return Response(
				"{ song_id: \"This field is required\" }",
				status=400
			)
		if playlist_id is None:
			return Response(
				"{ playlist_id: \"This field is required\" }",
				status=400
			)

		song = get_object_or_404(Song, pk=song_id)
		playlist = get_object_or_404(Playlist, playlist_id)
		playlist.songs.add(song)

		return Response()
