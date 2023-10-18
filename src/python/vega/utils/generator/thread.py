import typing
from threading import Thread

from apps.core.models import QueryParams, GenerationRequest
from utils.generator import Generator


class GenerationThread(Thread):

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

	def run(self) -> None:
		if self.__query_params is not None:
			self.__generator.generate(self.__query_params, self.__request)
			return
		self.__generator.generate_raw_query(self.__raw_query, self.__request)
