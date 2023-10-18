import typing

from utils.generator.executors.text.text_lm_executor import TextLMExecutor


class RawLyricsExecutor(TextLMExecutor):

	def _prepare_prompt_(self, query: str):
		return f"Write a lyrics for a track with the following description. {query}"

	def _prepare_output_(self, output: str) -> typing.Any:
		return output.strip()
