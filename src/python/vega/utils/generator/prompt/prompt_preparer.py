import typing
from abc import ABC, abstractmethod

from apps.core.models import QueryParams
from lib.gai_client import GAIClient


class GAIExecutor(ABC):

	def __init__(self, client: GAIClient):
		self.__client = client

	@abstractmethod
	def _prepare_prompt(self, *args, **kwargs) -> typing.Any:
		pass

	@abstractmethod
	def _prepare_output(self, output) -> typing.Any:
		pass

	def generate(self, *args, **kwargs):
		prompt = self._prepare_prompt(*args, **kwargs)
		output = self.__client.generate(prompt)
		return self._prepare_output(output)
