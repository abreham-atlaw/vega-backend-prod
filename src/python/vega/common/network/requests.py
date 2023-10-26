from typing import *

import json

from . import Serializer


# The Request class is used to create a request to a server.
class Request:

	# The Method class is used to define the HTTP methods that can be used in a request.
	class Method:
		GET = "GET"
		POST = "POST"
		PUT = "PUT"

	# The constructor method takes in several parameters to define the request.
	def __init__(
			self,
			url: str,
			get_params: Dict = None,
			post_data: object = None,
			files: dict = None,
			method: str = Method.GET,
			output_class: type = None,
			url_params=None,
			headers: Dict = None,
			content_type: Optional[str] = "application/json"
	):
		self.__url = url
		self.__method = method
		self.__get_params = get_params
		self.__serializer = Serializer(output_class)
		self.__post_data = post_data
		self.__url_params = url_params
		self.__headers = headers
		self.__files = files

		if post_data is None:
			self.__post_data = {}
		if get_params is None:
			self.__get_params = {}
		if url_params is None:
			self.__url_params = {}
		if method is None:
			self.__method = Request.Method.GET
		if headers is None:
			self.__headers = {}

	def get_url(self) -> str:
		return self.__url.format(**self.__url_params)  # Returns the URL of the request.

	def get_files(self) -> Optional[dict]:
		return self.__files  # Returns the files to be sent with the request.

	def get_get_params(self) -> Dict:
		return self.__get_params  # Returns the GET parameters of the request.

	def get_post_data(self) -> Dict:
		return self.__serializer.serialize(self.__post_data)  # Returns the POST data of the request.

	def get_method(self) -> str:
		return self.__method  # Returns the HTTP method of the request.

	def get_headers(self) -> Dict:
		return self.__headers  # Returns the headers of the request.

	def _filter_response(self, response):
		return response  # Filters the response (can be overridden by subclasses).

	def deserialize_object(self, response) -> object:
		return self.__serializer.deserialize(
			self._filter_response(
				response
			)
		)  # Deserializes the response into an object.
