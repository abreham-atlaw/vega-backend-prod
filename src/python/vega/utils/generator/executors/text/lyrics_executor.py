import typing

from features.core.models import QueryParams
from utils.generator.executors.text.text_lm_executor import TextLMExecutor


# LyricsExecutor is a class that inherits from TextLMExecutor and is used to generate lyrics.
class LyricsExecutor(TextLMExecutor):

	# This method prepares the output from the GAI model.
	# In this case, it removes leading and trailing whitespace from the output.
	def _prepare_output_(self, output) -> typing.Any:
		return output.strip()

	# This method prepares the prompt for the GAI model.
	# It takes in a QueryParams object and returns a string that describes the type of lyrics to be generated.
	def _prepare_prompt_(self, query_params: QueryParams, *args, **kwargs) -> typing.Any:
		return f"Write a lyrics for a {query_params.era} {query_params.genre} track with {query_params.mood} mood. It should be {', '.join(query_params.lyrics)}. It should also be suitable for an instrumental with {', '.join(query_params.instruments)}."
