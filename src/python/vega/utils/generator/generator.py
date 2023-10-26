import typing
from abc import abstractmethod, ABC

from features.authentication.models import VegaUser
from features.core.models import QueryParams, Song, GenerationRequest, Playlist
from dependency_injection.utils_providers import UtilsProviders


# Generator is an abstract base class that defines the structure for classes that generate music.
class Generator(ABC):

	# The constructor method initializes the recommender.
	def __init__(self):
		self.__recommender = UtilsProviders.provide_recommender()

	# This method updates the status of a generation request.
	def _update_status(self, request: GenerationRequest, status: GenerationRequest.Status):
		request.status = status.value
		request.save()

	# This is an abstract method that needs to be implemented by any class that inherits from Generator.
	# It should generate a song based on the given query parameters and generation request.
	@abstractmethod
	def generate(self, query_params: QueryParams, request: GenerationRequest):
		pass

	# This is an abstract method that needs to be implemented by any class that inherits from Generator.
	# It should generate a song based on the given raw query and generation request.
	@abstractmethod
	def generate_raw_query(self, query: str, request: GenerationRequest):
		pass

	# This is an abstract method that needs to be implemented by any class that inherits from Generator.
	# It should generate a title for a playlist based on the given songs and user.
	@abstractmethod
	def _generate_playlist_title(self, songs: typing.List[Song], user: VegaUser) -> str:
		pass

	# This method generates a playlist for a user.
	def generate_playlist(self, user: VegaUser) -> Playlist:
		params = self.__recommender.recommend(user)  # Get recommended parameters for the user.
		songs = [
			self.generate(
				param,
				GenerationRequest.objects.create()
			)
			for param in params  # Generate a song for each set of parameters.
		]
		title = self._generate_playlist_title(songs, user)  # Generate a title for the playlist.
		playlist = Playlist.objects.create(
			title=title,
			user=user  # Create a new playlist with the generated title and user.
		)
		playlist.songs.add(*songs)  # Add the generated songs to the playlist.

		return playlist  # Return the generated playlist.
