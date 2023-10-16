import typing

import re
from abc import ABC, abstractmethod

from apps.core.models import QueryParams
from utils.generator.executors.prompt_preparer import GAIExecutor


class TextLMExecutor(GAIExecutor, ABC):

	def __init__(self, *args, delimiter="```", **kwargs):
		super().__init__(*args, **kwargs)
		self.__delimiter = delimiter

	@abstractmethod
	def _prepare_prompt_(self, *args, **kwargs):
		pass

	@abstractmethod
	def _prepare_output_(self, output) -> typing.Any:
		pass

	def _prepare_prompt(self, *args, **kwargs) -> typing.Any:
		return f"{self._prepare_prompt_(*args, **kwargs)}. Wrap the response in {self.__delimiter}"

	def _prepare_output(self, output) -> typing.Any:
		return self._prepare_output_(self.__extract(output))

	def __extract(self, output) -> typing.Any:
		pattern = fr'{self.__delimiter}([\s\S]*)'
		match = re.search(pattern, output)
		if match:
			output = match.group(1)
			match = re.search(fr'([\s\S]*){self.__delimiter}', output)
			if match:
				return match.group(1)
			return output
		else:
			return output


class TextLMLyricsExecutor(TextLMExecutor):

	def _prepare_output_(self, output) -> typing.Any:
		return output.strip()

	def _prepare_prompt_(self, query_params: QueryParams, *args, **kwargs) -> typing.Any:
		return f"Write a lyrics for a {query_params.era} {query_params.genre} track with {query_params.mood} mood. It should be {', '.join(query_params.lyrics)}. It should also be suitable for an instrumental with {', '.join(query_params.instruments)}."


class TextLMTitleExecutor(TextLMExecutor):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, delimiter="\"", **kwargs)

	def _prepare_output_(self, output) -> typing.Any:
		return output[:40]

	def _restart(self, output, *args, **kwargs) -> bool:
		return output == ""

	def _prepare_prompt_(self, query_params: QueryParams, lyrics: str) -> typing.Any:
		return f"Give me one title for the track with these lyrics\n\n{lyrics}."
