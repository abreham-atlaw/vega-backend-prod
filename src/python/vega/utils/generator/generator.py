from abc import abstractmethod, ABC

from apps.core.models import QueryParams, Song, GenerationRequest


class Generator(ABC):

	def _update_status(self, request: GenerationRequest, status: GenerationRequest.Status):
		request.status = status.value
		request.save()

	@abstractmethod
	def generate(self, query_params: QueryParams, request: GenerationRequest):
		pass

	def generate_raw_query(self, query: str, request: GenerationRequest):
		pass
