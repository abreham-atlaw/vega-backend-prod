import typing
from abc import ABC, abstractmethod


# GAI(GenerativeAI) is an abstract class that is meant to be used for consistent generation calls with multiple
# generative models
class GAI(ABC):

	@abstractmethod
	def generate(self, *args, **kwargs) -> typing.Any:
		pass