import typing

from utils.generator.executors.prompt_preparer import GAIExecutor


class MusicGenRawExecutor(GAIExecutor):

	def _prepare_prompt(self, query: str) -> typing.Any:
		return f"{query}"

	def _prepare_output(self, output) -> typing.Any:
		return output