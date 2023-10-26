import typing

from features.core.models import Song
from utils.generator.executors.text import TextLMExecutor


class PlaylistTitleExecutor(TextLMExecutor):

	def _prepare_prompt_(self, songs: typing.List[Song]):
		return f"""
Give me a title for a playlist with the following track names in it:
{', '.join([song.title for song in songs])}
"""

	def _prepare_output_(self, output) -> typing.Any:
		return output

	def _restart(self, output, *args, **kwargs) -> bool:
		return output == ""
