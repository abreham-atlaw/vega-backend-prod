import typing

import re
from abc import ABC, abstractmethod

from apps.core.models import QueryParams
from utils.generator.executors.prompt_preparer import GAIExecutor
from utils.generator.executors.text.text_lm_executor import TextLMExecutor


class TitleExecutor(TextLMExecutor):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, delimiter="\"", **kwargs)

	def _prepare_output_(self, output) -> typing.Any:
		return output[:40]

	def _restart(self, output, *args, **kwargs) -> bool:
		return output == ""

	def _prepare_prompt_(self, lyrics: str) -> typing.Any:
		return f"Give me one title for the track with these lyrics\n\n{lyrics}."
