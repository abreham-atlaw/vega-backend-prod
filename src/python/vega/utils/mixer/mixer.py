import datetime
import os.path
from abc import abstractmethod, ABC


# Define an abstract base class named Mixer
class Mixer(ABC):

	# Initialize the Mixer object with an export path, default is current directory
	def __init__(self, export_path: str = "./"):
		self.__export_path = export_path

	# Private method to generate a file path for the output file
	def _generate_filepath(self) -> str:
		# Create a filename using the current timestamp and .wav extension
		filename = f"{datetime.datetime.now().timestamp()}.wav"
		# Join the export path and the filename to create a full file path
		return os.path.join(self.__export_path, filename)

	# Abstract method to be implemented by subclasses, for mixing instrumental and vocal tracks
	@abstractmethod
	def _mix(self, instrumental_path: str, vocal_path: str, output_path: str):
		pass

	# Public method to mix two tracks and return the output file path
	def mix(self, instrumental_path: str, vocal_path: str) -> str:
		# Generate a file path for the output file
		output_path = self._generate_filepath()
		# Call the _mix method (to be implemented by subclasses) with the input and output paths
		self._mix(instrumental_path, vocal_path, output_path)
		# Return the output file path
		return output_path
