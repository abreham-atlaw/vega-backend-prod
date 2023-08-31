
from django.urls import path

from apps.core.views import GenerateView, SongDetailView
from apps.core.views.generate import GenerationStatusView

urlpatterns = [
	path("song/generate/", GenerateView.as_view()),
	path("song/status/", GenerationStatusView.as_view()),
	path("song/detail/", SongDetailView.as_view())
]
