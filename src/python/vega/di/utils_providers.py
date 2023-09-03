from utils.generator import MockGenerator
from utils.generator.generator import Generator
from utils.mixer.audiodub import AudiodubMixer
from utils.mixer.mock_mixer import MockMixer
from vega.settings import TMP_PATH
from utils.mixer.mixer import Mixer


class UtilsProviders:

	@staticmethod
	def provide_generator() -> Generator:
		from utils.generator.gai_generator import GAIGenerator
		return GAIGenerator()

	@staticmethod
	def provide_mixer() -> 'Mixer':
		return AudiodubMixer(export_path=TMP_PATH)
