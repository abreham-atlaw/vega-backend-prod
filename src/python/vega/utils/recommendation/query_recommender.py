import typing
from abc import ABC, abstractmethod

from django.contrib.auth.models import User

from apps.core.models import QueryParamsSample


class QueryRecommender(ABC):

	@abstractmethod
	def recommend(self, user: User) -> typing.List[QueryParamsSample]:
		pass
