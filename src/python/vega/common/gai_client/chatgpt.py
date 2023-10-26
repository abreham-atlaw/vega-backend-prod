import typing
import openai
import time

from common.gai_client.gai import GAI


# ChatGPT is a class that inherits from GAI
class ChatGPT(GAI):

	# The constructor method takes in a token and system as parameters
	def __init__(self, token: str, system: str, *args, **kwargs):
		super().__init__(*args, **kwargs)
		openai.api_key = token  # Set the OpenAI API key
		self.__system = system  # Set the system message

	# This method generates a response from the GPT-3 model for a given message.
	def generate(self, message) -> typing.Any:

		try:
			# Create a chat completion with the GPT-3 model
			response = openai.ChatCompletion.create(
				model="gpt-3.5-turbo",
				messages=[
					{
						"role": "system",
						"content": self.__system  # System message
					},
					{
						"role": "user",
						"content": message  # User message
					}
				]
			)
			return response.choices[0].message.content  # Return the content of the first choice
		except openai.error.RateLimitError:
			time.sleep(70)  # If rate limit is exceeded, wait for 70 seconds
			return self.generate(message)  # Try generating the response again after waiting
