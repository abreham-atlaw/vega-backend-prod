import typing
from abc import ABC, abstractmethod

from features.authentication.models import VegaUser
from features.core.models import QueryParamsSample


class QueryRecommender(ABC):

	@abstractmethod
	def recommend(self, user: VegaUser) -> typing.List[QueryParamsSample]:
		pass
