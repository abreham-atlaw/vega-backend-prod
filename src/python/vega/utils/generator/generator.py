from abc import abstractmethod, ABC

from apps.core.models import QueryParams, Song, GenerationRequest


class Generator(ABC):

	@abstractmethod
	def generate(self, query_params: QueryParams, request: GenerationRequest) -> Song:
		pass
