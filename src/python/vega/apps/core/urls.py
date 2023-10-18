
from django.urls import path

from apps.core.views import GenerateView, SongDetailView
from apps.core.views.generate import GenerationStatusView, RecommendationsView, RawGenerateView
from apps.core.views.song import RecentSongsView

urlpatterns = [
	path("song/generate/", GenerateView.as_view()),
	path("song/generate-raw/", RawGenerateView.as_view()),

	path("song/status/", GenerationStatusView.as_view()),
	path("song/detail/", SongDetailView.as_view()),
	path("song/recent/", RecentSongsView.as_view()),

	path("query/recommendations/", RecommendationsView.as_view())
]
