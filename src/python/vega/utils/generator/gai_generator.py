import os.path
import random
import typing

from features.authentication.models import VegaUser
from features.core.models import QueryParams, GenerationRequest, Song
from dependency_injection.lib_providers import LibProviders
from dependency_injection.utils_providers import UtilsProviders
from utils.generator import Generator
from utils.generator.executors.bark import BarkExecutor
from utils.generator.executors.instrumental import MusicGenRawExecutor, MusicGenExecutor
from utils.generator.executors.text import LyricsExecutor, TitleExecutor, RawLyricsExecutor
from utils.generator.executors.text.playlist_title_executor import PlaylistTitleExecutor


# GAIGenerator is a class that inherits from Generator and is used to generate music.
class GAIGenerator(Generator):

	# The constructor method initializes the music generator, text language model, bark client,
	# instrumental executor, instrumental raw executor, bark executor, lyrics executor,
	# raw lyrics executor, title executor, playlist title executor, mixer and file storage.
	def __init__(self):
		super().__init__()
		self.__music_gen = LibProviders.provide_musicgen_client()
		self.__text_lm = LibProviders.provide_llama2()
		self.__bark = LibProviders.provide_bark_client()

		self.__instrumental_executor = MusicGenExecutor(self.__music_gen)
		self.__instrumental_raw_executor = MusicGenRawExecutor(self.__music_gen)
		self.__bark_executor = BarkExecutor(self.__bark)
		self.__lyrics_executor = LyricsExecutor(self.__text_lm)
		self.__raw_lyrics_executor = RawLyricsExecutor(self.__text_lm)
		self.__title_executor = TitleExecutor(self.__text_lm)
		self.__playlist_title_executor = PlaylistTitleExecutor(self.__text_lm)

		self.__mixer = UtilsProviders.provide_mixer()
		self.__file_storage = LibProviders.provide_file_storage()

	# These methods generate instrumental and lyrics based on the given query.
	def __generate_instrumental(self, query: typing.Union[QueryParams, str], raw=False) -> str:
		if raw:
			return self.__instrumental_raw_executor.generate(query)
		return self.__instrumental_executor.generate(query)

	def __generate_lyrics(self, query: typing.Union[QueryParams, str], raw=False) -> str:
		if raw:
			return self.__raw_lyrics_executor.generate(query)
		return self.__lyrics_executor.generate(query)

	# temporary placeholder for generating song cover image
	def __generate_cover(self) -> str:
		return random.choice([
			"https://dl.dropboxusercontent.com/scl/fi/ogc9g25l9gebvj6r7uj1g/_91259a40-5cf1-4bf0-bcfb-6d450d8525df.jpeg?rlkey=4vkx18bfwkvn854gio174kwm7&dl=0",
			"https://dl.dropboxusercontent.com/scl/fi/xgjlkx4sh3g2bnxg3eixu/_e410fab7-e6b1-4089-9b55-b68f24858394.jpeg?rlkey=enkqklcme40zmm7soblw4xgps&dl=0",
			"https://dl.dropboxusercontent.com/scl/fi/gxx3bdmhq59uy7fknx3ta/_296dff94-512e-4926-91d8-dc8e0c59310a.jpeg?rlkey=gjpswlh27sc308cg80t3ne35r&dl=0",
			"https://dl.dropboxusercontent.com/scl/fi/40rvexwnuebe3ivj8uzv8/_abb99a3e-7bed-4291-a37a-9f4d9b2d6370.jpeg?rlkey=r89d15otwgbagixtwov9hm7yq&dl=0",
			"https://dl.dropboxusercontent.com/scl/fi/d00ptbdoyco9cemfw86im/_a4506d91-1859-46e4-950d-f832b3baa55a.jpeg?rlkey=knocj8sa0li1yr1ksg8derfd1&dl=0",
			"https://dl.dropboxusercontent.com/scl/fi/0c7kvwyiqx7fn16rvlyhv/_3ccb8f82-5513-4d83-b12a-e674ea6c5e9d.jpeg?rlkey=u1w2woa1zp1b8kceix7iwausi&dl=0",
			"https://dl.dropboxusercontent.com/scl/fi/hqojaknkzxs8h4988p6my/_f129b198-2b0c-4f59-a95a-2a27cefa72fc.jpeg?rlkey=m93hxgzd8e3v7skmws0h93ypl&dl=0",
			"https://dl.dropboxusercontent.com/scl/fi/te5aof21n7kh5udh5rwh5/_caa7f7aa-59d6-4b17-8985-56f6d65a70e6.jpeg?rlkey=gbw1vob38b2zo2ijntkrwgfea&dl=0",
			"https://dl.dropboxusercontent.com/scl/fi/9i3fz4o020og759ji3odj/_e49c8ee0-77f7-4448-bd7f-0a3189edcebf.jpeg?rlkey=cjesrr2p36mer4q8ut76ddhrq&dl=0",
			"https://dl.dropboxusercontent.com/scl/fi/4bulr7oqkc2hv0q4z3xzr/_a34afc48-aec4-4625-8dd8-62a2edbf5cbe.jpeg?rlkey=rcgvy8fqyiglimi9g9c3bqmlc&dl=0",
			"https://dl.dropboxusercontent.com/scl/fi/azwmi151vnbr8tyz9nnpm/_f3325b15-9b28-4ff2-9308-1cc1a92fafc0.jpeg?rlkey=wm1vp8y6xleicz4gtx7udmsf5&dl=0",
			"https://dl.dropboxusercontent.com/scl/fi/qqhb3q6ipdy9d07obht6g/_79557855-b73a-4ffd-8706-0fad7879d846.jpeg?rlkey=zlz16u2y8hqwgmb5tcvudx2ys&dl=0",
			"https://dl.dropboxusercontent.com/scl/fi/h4hdnaldml1ldse0ppr7j/_59dd85fa-32ef-4667-bd73-02e4da05d5a2.jpeg?rlkey=g0nxmz1h8026yb76id58gnqfz&dl=0",
			"https://dl.dropboxusercontent.com/scl/fi/351cd80hfwyg8wrb1wnsx/_84dc5c25-883c-47f9-8c1f-559a19516ce2.jpeg?rlkey=1hrw7562goqnju29ia2ogwlvk&dl=0",
			"https://dl.dropboxusercontent.com/scl/fi/ovhfjpn7420jbhew49889/_4ef53fec-637e-4ccd-834b-a11d089566a1.jpeg?rlkey=sg26w7nu3yf8e7yiivxy90fee&dl=0"
		])

	# This method generates a song based on the given query and request.
	def __generate(self, query: typing.Union[QueryParams, str], request: GenerationRequest, raw=False) -> Song:

		self._update_status(request, GenerationRequest.Status.instrumental)
		instrumental = self.__generate_instrumental(query, raw=raw)

		self._update_status(request, GenerationRequest.Status.lyrics)
		lyrics = self.__generate_lyrics(query, raw=raw)

		title = self.__title_executor.generate(lyrics)

		self._update_status(request, GenerationRequest.Status.vocal)
		vocals = self.__bark_executor.generate(lyrics)

		self._update_status(request, GenerationRequest.Status.mix)
		mix = self.__mixer.mix(instrumental, vocals)
		self.__file_storage.upload_file(mix)
		audio_url = self.__file_storage.get_url(os.path.basename(mix))

		cover = self.__generate_cover()

		song = Song(
			title=title,
			audio=audio_url,
			cover=cover,
			lyrics=lyrics,
			duration=15.0
		)
		song.save()

		request.song = song
		self._update_status(request, GenerationRequest.Status.done)
		return song

	def generate(self, query_params: QueryParams, request: GenerationRequest) -> Song:
		return self.__generate(query_params, request, raw=False)

	def generate_raw_query(self, query: str, request: GenerationRequest) -> Song:
		return self.__generate(query, request, raw=True)

	def _generate_playlist_title(self, songs: typing.List[Song], user: VegaUser) -> str:
		return self.__playlist_title_executor.generate(songs)
