import typing
from threading import Thread

from features.core.models import QueryParams, GenerationRequest
from utils.generator import Generator


# GenerationThread is a class that inherits from Thread and is used to generate music in a separate thread.
class GenerationThread(Thread):

	# The constructor method takes in a generator, a generation request, query parameters, and a raw query as parameters.
	def __init__(
			self,
			generator: Generator,
			request: GenerationRequest,
			*args,
			query_params: typing.Optional[QueryParams] = None,
			raw_query: typing.Optional[str] = None,
			**kwargs
	):
		super().__init__(*args, **kwargs)
		self.__query_params = query_params
		self.__raw_query = raw_query
		if raw_query is None and query_params is None:
			raise ValueError("Either raw query or QueryParam required")
		self.__generator = generator
		self.__request = request

	# This method runs the thread.
	def run(self) -> None:
		if self.__query_params is not None:
			self.__generator.generate(self.__query_params, self.__request)
			return
		self.__generator.generate_raw_query(self.__raw_query, self.__request)
