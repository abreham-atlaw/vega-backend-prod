import typing

import re

from utils.generator.executors.prompt_preparer import GAIExecutor


# BarkExecutor is a class that inherits from GAIExecutor and is used to generate vocals.
class BarkExecutor(GAIExecutor):

	# This method prepares the output from the GAI model.
	# In this case, it simply returns the output as it is.
	def _prepare_output(self, output) -> typing.Any:
		return output

	# This static method removes any text within parentheses from the input text.
	@staticmethod
	def extract_lyrics(text):
		cleaned_text = re.sub(r'\(.*?\)', '', text)
		cleaned_text = cleaned_text.strip()
		return cleaned_text

	# This static method formats the lyrics by removing any text within parentheses and splitting the lyrics into verses.
	@staticmethod
	def __format_lyrics(lyrics: str):
		cleaned = BarkExecutor.extract_lyrics(lyrics)
		return cleaned.split("\n\n")[0].replace("\n", " ")

	# This method prepares the prompt for the GAI model.
	# It takes in a string of lyrics and returns a string that describes the type of lyrics to be vocalized.
	def _prepare_prompt(self, lyrics: str) -> typing.Any:
		return f"♪ [rap] {self.__format_lyrics(lyrics)} [rap] ♪"
