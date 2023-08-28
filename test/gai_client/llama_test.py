import unittest

from gai_client.llama2 import LlamaClient


class LlamaClientTest(unittest.TestCase):

	def test_functionality(self):

		# Make sure the Llama2Processor is running when running this test
		client = LlamaClient("https://llmchat-server.vercel.app/api")
		response = client("Write a poem about a man named Biruk Aynalem who has the powers of Zues")
		print(response)
