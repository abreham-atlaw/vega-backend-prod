
from django.urls import path

from features.authentication.views import LoginView, SignupView, UserExistsView, WhoAmIView


urlpatterns = [
	path("signup/", SignupView.as_view()),
	path("login/", LoginView.as_view()),
	path("user-exists/", UserExistsView.as_view()),
	path("me/", WhoAmIView.as_view())
]
