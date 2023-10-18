import typing

from apps.core.models import QueryParams
from utils.generator.executors.prompt_preparer import GAIExecutor


class MusicGenExecutor(GAIExecutor):

	def _prepare_output(self, output) -> typing.Any:
		return output

	def _prepare_prompt(self, query_params: QueryParams) -> typing.Any:
		return f"A {query_params.mood} {query_params.era} {query_params.genre} song with {', '.join(query_params.instruments)} and made for {', '.join(query_params.lyrics)} lyrics"
