import os.path

from apps.core.models import QueryParams, GenerationRequest, Song
from di.lib_providers import LibProviders
from di.utils_providers import UtilsProviders
from utils.generator import Generator
from utils.generator.prompt.bark import BarkExecutor
from utils.generator.prompt.llama2 import Llama2LyricsExecutor, Llama2TitleExecutor
from utils.generator.prompt.musicgen import MusicGenPreparer


class GAIGenerator(Generator):

	def __init__(self):
		self.__music_gen = LibProviders.provide_musicgen_client()
		self.__llama2 = LibProviders.provide_llama2()
		self.__bark = LibProviders.provide_bark_client()

		self.__music_gen_executor = MusicGenPreparer(self.__music_gen)
		self.__bark_executor = BarkExecutor(self.__bark)
		self.__llama2_executor = Llama2LyricsExecutor(self.__llama2)
		self.__llama2_title_executor = Llama2TitleExecutor(self.__llama2)

		self.__mixer = UtilsProviders.provide_mixer()
		self.__file_storage = LibProviders.provide_file_storage()

	def generate(self, query_params: QueryParams, request: GenerationRequest) -> Song:
		self._update_status(request, GenerationRequest.Status.lyrics)
		lyrics = self.__llama2_executor.generate(query_params)
		title = self.__llama2_title_executor.generate(query_params, lyrics)

		self._update_status(request, GenerationRequest.Status.vocal)
		vocals = self.__bark_executor.generate(query_params, lyrics)

		self._update_status(request, GenerationRequest.Status.instrumental)
		instrumental = self.__music_gen_executor.generate(query_params)



		self._update_status(request, GenerationRequest.Status.mix)
		mix = self.__mixer.mix(instrumental, vocals)
		self.__file_storage.upload_file(mix)
		audio_url = self.__file_storage.get_url(os.path.basename(mix))

		song = Song(
			title=title,
			audio=audio_url,
			cover="https://www.dropbox.com/scl/fi/65jq2zoqg5l3o203aprq4/1693508148.414699.png?rlkey=bfngqxunb01xm86dam00xe3o8&dl=0&raw=1",
			lyrics=lyrics
		)
		song.save()

		request.song = song
		self._update_status(request, GenerationRequest.Status.done)
