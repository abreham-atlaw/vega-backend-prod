import typing
from abc import ABC, abstractmethod

from .gai import GAI
from .requests import CreateRequest, FetchResponseRequest
from common.network.client import NetworkApiClient


# GAIClient is a class that inherits from GAI, NetworkApiClient and ABC (Abstract Base Class)
class GAIClient(GAI, NetworkApiClient, ABC):

	# The constructor method takes in a url and model_id as parameters
	def __init__(self, url: str, model_id: str):
		super().__init__(url=url)
		self.__model_id = model_id

	# This is an abstract method that needs to be implemented by any class that inherits from GAIClient.
	# It should generate parameters for a request.
	@abstractmethod
	def _generate_params(self, *args, **kwargs) -> typing.Dict:
		pass

	# This is an abstract method that needs to be implemented by any class that inherits from GAIClient.
	# It should deserialize the response received from the server.
	@abstractmethod
	def _deserialize_response(self, response: typing.Any) -> typing.Any:
		pass

	# This private method sends a FetchResponseRequest until it gets a response.
	def __get_response(self, request_id: str):
		print("[+]Waiting for response...")
		response = None
		while response is None:
			response = self.execute(
				FetchResponseRequest(
					request_id=request_id
				)
			)
		return response

	# This method generates parameters for a request, sends a CreateRequest and waits for the response.
	def generate(self, *args, **kwargs):
		params = self._generate_params(*args, **kwargs)
		request_id = self.execute(
			CreateRequest(
				model_id=self.__model_id,
				params=params
			)
		)

		response = self.__get_response(request_id)
		return  self._deserialize_response(response)

	# This method allows an instance of GAIClient to be called like a function.
	def __call__(self, *args, **kwargs):
		return self.generate(*args, **kwargs)
