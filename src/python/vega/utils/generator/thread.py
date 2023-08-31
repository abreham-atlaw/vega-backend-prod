from threading import Thread

from apps.core.models import QueryParams, GenerationRequest
from utils.generator import Generator


class GenerationThread(Thread):

	def __init__(
			self,
			query_params: QueryParams,
			generator: Generator,
			request: GenerationRequest,
			*args,
			**kwargs
	):
		super().__init__(*args, **kwargs)
		self.__query_params = query_params
		self.__generator = generator
		self.__request = request

	def run(self) -> None:
		self.__generator.generate(self.__query_params, self.__request)
