from utils.generator import MockGenerator
from utils.generator.generator import Generator


class UtilsProviders:

	@staticmethod
	def provide_generator() -> Generator:
		return MockGenerator()
