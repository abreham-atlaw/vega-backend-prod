from utils.generator import MockGenerator
from utils.generator.generator import Generator
from utils.mixer.audiodub import AudiodubMixer
from utils.mixer.mock_mixer import MockMixer
from utils.recommendation.mock_query_recommender import MockQueryRecommender
from utils.recommendation.query_recommender import QueryRecommender
from vega.settings import TMP_PATH
from utils.mixer.mixer import Mixer


class UtilsProviders:

	@staticmethod
	def provide_generator() -> Generator:
		from utils.generator.gai_generator import GAIGenerator
		from utils.generator.mock_generator import MockGenerator
		return GAIGenerator()

	@staticmethod
	def provide_mixer() -> 'Mixer':
		return AudiodubMixer(export_path=TMP_PATH)

	@staticmethod
	def provide_recommender() -> QueryRecommender:
		return MockQueryRecommender()
