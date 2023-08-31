import typing

import unittest

from gai_client.client import GAIClient


class TestGAIClient(GAIClient):

	def __init__(self, url: str):
		super().__init__(url, "test")

	def _generate_params(self, query) -> typing.Dict:
		return {
			"query": query
		}

	def _deserialize_response(self, response: typing.Any) -> typing.Any:
		return response


class GAIClientTest(unittest.TestCase):

	def test_functionality(self):
		client = TestGAIClient("https://llmchat-server.vercel.app/api")
		response = client("hello")
		print(response)
