from abc import ABC

import requests
from urllib.parse import urlparse
import os

from .client import GAIClient


# Define a class FileBasedClient that inherits from GAIClient and ABC
class FileBasedClient(GAIClient, ABC):

    # Initialize the class with arguments and keyword arguments
    def __init__(self, *args, out_path="./", **kwargs):
        # Call the parent class initializer
        super().__init__(*args, **kwargs)
        # Set the output path to an absolute path
        self.__out_path = os.path.abspath(out_path)

    # Define a static method to download a file from a URL
    @staticmethod
    def __download_file(url, directory_path):
        print(f"[+]Downloading {url}...")
        # Parse the URL to get the filename
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # Join the directory path and filename to get the full file path
        file_path = os.path.join(directory_path, filename)

        # Send a GET request to the URL
        response = requests.get(url)
        # Raise an HTTPError if one occurred
        response.raise_for_status()

        # Open the file in write-binary mode and write the content of the response to it
        with open(file_path, 'wb') as file:
            file.write(response.content)

        # Return the file path
        return file_path

    # Define a method to deserialize a response string by downloading it as a file
    def _deserialize_response(self, response: str) -> str:
        return self.__download_file(response, self.__out_path)
