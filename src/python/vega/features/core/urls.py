
from django.urls import path

from features.core.views import GenerateView, SongDetailView, CreatePlaylistView, PlaylistDetailView, PlaylistListView, \
	AddToPlaylistView
from features.core.views.generate import GenerationStatusView, RecommendationsView, RawGenerateView
from features.core.views.song import RecentSongsView

urlpatterns = [
	path("song/generate/", GenerateView.as_view()),
	path("song/generate-raw/", RawGenerateView.as_view()),

	path("song/status/", GenerationStatusView.as_view()),
	path("song/detail/", SongDetailView.as_view()),
	path("song/recent/", RecentSongsView.as_view()),

	path("playlist/create/", CreatePlaylistView.as_view()),
	path("playlist/detail/", PlaylistDetailView.as_view()),
	path("playlist/all/", PlaylistListView.as_view()),
	path("playlist/add/", AddToPlaylistView.as_view()),

	path("query/recommendations/", RecommendationsView.as_view()),
]
