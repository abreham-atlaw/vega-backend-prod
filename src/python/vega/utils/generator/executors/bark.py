import typing

import re

from apps.core.models import QueryParams
from utils.generator.executors.prompt_preparer import GAIExecutor


class BarkExecutor(GAIExecutor):

	def _prepare_output(self, output) -> typing.Any:
		return output

	@staticmethod
	def extract_lyrics(text):
		cleaned_text = re.sub(r'\(.*?\)', '', text)
		cleaned_text = cleaned_text.strip()
		return cleaned_text

	@staticmethod
	def __format_lyrics(lyrics: str):
		cleaned = BarkExecutor.extract_lyrics(lyrics)
		return cleaned.split("\n\n")[0].replace("\n", " ")

	def _prepare_prompt(self, query_params: QueryParams, lyrics: str) -> typing.Any:
		return f"♪ [rap] {self.__format_lyrics(lyrics)} [rap] ♪"
