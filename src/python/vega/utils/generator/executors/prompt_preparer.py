import typing
from abc import ABC, abstractmethod

from common.gai_client.gai import GAI


# GAIExecutor is an abstract base class that defines the structure for classes that execute GAI models.
class GAIExecutor(ABC):

	# The constructor method takes in a client as a parameter.
	def __init__(self, client: GAI):
		self.__client = client

	# This is an abstract method that needs to be implemented by any class that inherits from GAIExecutor.
	# It should prepare the prompt for the GAI model.
	@abstractmethod
	def _prepare_prompt(self, *args, **kwargs) -> typing.Any:
		pass

	# This is an abstract method that needs to be implemented by any class that inherits from GAIExecutor.
	# It should prepare the output from the GAI model.
	@abstractmethod
	def _prepare_output(self, output) -> typing.Any:
		pass

	# This method checks if the generation process needs to be restarted based on the output.
	# By default, it returns False but can be overridden by subclasses.
	def _restart(self, output, *args, **kwargs) -> bool:
		return False

	# This method generates an output from the GAI model.
	def generate(self, *args, **kwargs):
		prompt = self._prepare_prompt(*args, **kwargs)
		output = self.__client.generate(prompt)
		output = self._prepare_output(output)
		if self._restart(output, *args, **kwargs):
			return self.generate(*args, **kwargs)
		return output
