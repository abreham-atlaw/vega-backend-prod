import os.path
import typing

from apps.core.models import QueryParams, GenerationRequest, Song
from di.lib_providers import LibProviders
from di.utils_providers import UtilsProviders
from utils.generator import Generator
from utils.generator.executors.bark import BarkExecutor
from utils.generator.executors.instrumental import MusicGenRawExecutor, MusicGenExecutor
from utils.generator.executors.text import LyricsExecutor, TitleExecutor, RawLyricsExecutor


class GAIGenerator(Generator):

	def __init__(self):
		self.__music_gen = LibProviders.provide_musicgen_client()
		self.__text_lm = LibProviders.provide_llama2()
		self.__bark = LibProviders.provide_bark_client()

		self.__instrumental_executor = MusicGenExecutor(self.__music_gen)
		self.__instrumental_raw_executor = MusicGenRawExecutor(self.__music_gen)
		self.__bark_executor = BarkExecutor(self.__bark)
		self.__lyrics_executor = LyricsExecutor(self.__text_lm)
		self.__raw_lyrics_executor = RawLyricsExecutor(self.__text_lm)
		self.__title_executor = TitleExecutor(self.__text_lm)

		self.__mixer = UtilsProviders.provide_mixer()
		self.__file_storage = LibProviders.provide_file_storage()

	def __generate_instrumental(self, query: typing.Union[QueryParams, str], raw=False) -> str:
		if raw:
			return self.__instrumental_raw_executor.generate(query)
		return self.__instrumental_executor.generate(query)

	def __generate_lyrics(self, query: typing.Union[QueryParams, str], raw=False) -> str:
		if raw:
			return self.__raw_lyrics_executor.generate(query)
		return self.__lyrics_executor.generate(query)

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

		song = Song(
			title=title,
			audio=audio_url,
			cover="https://dl.dropboxusercontent.com/scl/fi/yp5goz0c3f9bezv1lrc0x/02.png?rlkey=jh8thuix6kb1n65q8cuy1em16&dl=0&raw=1",
			lyrics=lyrics
		)
		song.save()

		request.song = song
		self._update_status(request, GenerationRequest.Status.done)
		return song

	def generate(self, query_params: QueryParams, request: GenerationRequest) -> Song:
		return self.__generate(query_params, request, raw=False)

	def generate_raw_query(self, query: str, request: GenerationRequest) -> Song:
		return self.__generate(query, request, raw=True)
