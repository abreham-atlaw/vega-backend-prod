import typing

from gai_client.client import GAIClient


class LlamaClient(GAIClient):

	def __init__(self, url: str):
		super().__init__(url, model_id="llama2")

	def _generate_params(self, message: str) -> typing.Dict:
		return {
			"query": message
		}

	def _deserialize_response(self, response: typing.Any) -> typing.Any:
		return response
