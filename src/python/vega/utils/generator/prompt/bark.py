import typing

from apps.core.models import QueryParams
from utils.generator.prompt.prompt_preparer import GAIExecutor


class BarkExecutor(GAIExecutor):

	def _prepare_output(self, output) -> typing.Any:
		return output

	def _prepare_prompt(self, query_params: QueryParams, lyrics: str) -> typing.Any:
		return f"♪ {lyrics[:100]} ♪"
