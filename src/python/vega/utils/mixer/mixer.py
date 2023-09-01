import datetime
import os.path
from abc import abstractmethod, ABC


class Mixer(ABC):

	def __init__(self, export_path: str = "./"):
		self.__export_path = export_path

	def _generate_filepath(self) -> str:
		filename = f"{datetime.datetime.now().timestamp()}.wav"
		return os.path.join(self.__export_path, filename)

	@abstractmethod
	def _mix(self, instrumental_path: str, vocal_path: str, output_path: str):
		pass

	def mix(self, instrumental_path: str, vocal_path: str) -> str:
		output_path = self._generate_filepath()
		self._mix(instrumental_path, vocal_path, output_path)
		return output_path
