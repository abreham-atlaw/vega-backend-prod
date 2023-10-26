import typing

from features.core.models import QueryParams
from utils.generator.executors.prompt_preparer import GAIExecutor


# MusicGenExecutor is a class that inherits from GAIExecutor and is used to generate music.
class MusicGenExecutor(GAIExecutor):

	# This method prepares the output from the GAI model.
	# In this case, it simply returns the output as it is.
	def _prepare_output(self, output) -> typing.Any:
		return output

	# This method prepares the prompt for the GAI model.
	# It takes in a QueryParams object and returns a string that describes the type of music to be generated.
	def _prepare_prompt(self, query_params: QueryParams) -> typing.Any:
		return f"A {query_params.mood} {query_params.era} {query_params.genre} song with {', '.join(query_params.instruments)} and made for {', '.join(query_params.lyrics)} lyrics"
