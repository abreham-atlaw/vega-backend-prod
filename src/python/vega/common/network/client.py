from typing import *

import requests
from requests.exceptions import HTTPError

from . import Request
from .exceptions import InvalidNetworkMethod


# The NetworkApiClient class is used to send HTTP requests to a server.
class NetworkApiClient:

	# The constructor method takes in a url and timeout as parameters.
	def __init__(self, url: str, timeout=None):
		self.__url = url
		if url.endswith("/"):
			self.__url = url[:-1]
		self.__timeout = timeout

	def _get_complete_url(self, url):
		if url.startswith("/"):
			url = url[1:]
		return f"{self.__url}/{url}"  # Returns the complete URL for the request.

	def _get(self, request: Request, headers=None):
		return requests.get(
			self._get_complete_url(request.get_url()),
			params=request.get_get_params(),
			headers=headers,
			timeout=self.__timeout
		)  # Sends a GET request to the server.

	def _post(self, request: Request, headers=None):
		files = None
		try:
			if request.get_files() is not None:
				files = {
					key: open(filename, "rb")
					for key, filename in
					request.get_files().items()
				}
			response = requests.post(
				self._get_complete_url(request.get_url()),
				data=request.get_post_data(),
				params=request.get_get_params(),
				headers=headers,
				files=files,
				timeout=self.__timeout
			)
		finally:
			if files is not None:
				for _, file in files.items():
					file.close()
		return response  # Sends a POST request to the server.

	def _put(self, request: Request, headers=None):
		return requests.put(
			self._get_complete_url(request.get_url()),
			data=request.get_post_data(),
			headers=headers,
			timeout=self.__timeout
		)  # Sends a PUT request to the server.

	def execute(self, request: Request, headers: Optional[Dict] = None):
		if headers is None:
			headers = {
				"Content-Type": "application/json"
			}
		response = None
		headers.update(request.get_headers())
		if request.get_method() == Request.Method.GET:
			response = self._get(request, headers=headers)
		elif request.get_method() == Request.Method.POST:
			response = self._post(request, headers=headers)
		elif request.get_method() == Request.Method.PUT:
			response = self._put(request, headers=headers)
		else:
			raise InvalidNetworkMethod()

		if 400 <= response.status_code < 600:
			raise HTTPError(f"Status Code: {response.status_code} Message: {response.text}")
		if response.text == "":
			return None
		return request.deserialize_object(response.json())  # Executes the request and returns the response.
