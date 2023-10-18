import typing

from apps.core.models import QueryParams
from utils.generator.executors.text.text_lm_executor import TextLMExecutor


class LyricsExecutor(TextLMExecutor):

	def _prepare_output_(self, output) -> typing.Any:
		return output.strip()

	def _prepare_prompt_(self, query_params: QueryParams, *args, **kwargs) -> typing.Any:
		return f"Write a lyrics for a {query_params.era} {query_params.genre} track with {query_params.mood} mood. It should be {', '.join(query_params.lyrics)}. It should also be suitable for an instrumental with {', '.join(query_params.instruments)}."

