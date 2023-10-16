import typing
from abc import ABC, abstractmethod

from apps.core.models import QueryParams
from lib.gai_client import GAIClient
from lib.gai_client.gai import GAI


class GAIExecutor(ABC):

	def __init__(self, client: GAI):
		self.__client = client

	@abstractmethod
	def _prepare_prompt(self, *args, **kwargs) -> typing.Any:
		pass

	@abstractmethod
	def _prepare_output(self, output) -> typing.Any:
		pass

	def _restart(self, output, *args, **kwargs) -> bool:
		return False

	def generate(self, *args, **kwargs):
		prompt = self._prepare_prompt(*args, **kwargs)
		output = self.__client.generate(prompt)
		output = self._prepare_output(output)
		if self._restart(output, *args, **kwargs):
			return self.generate(*args, **kwargs)
		return output
