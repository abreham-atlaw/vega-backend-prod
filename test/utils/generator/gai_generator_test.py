import unittest

from features.core.models import QueryParams
from dependency_injection.utils_providers import UtilsProviders


class GAIGeneratorTest(unittest.TestCase):

	def test_functionality(self):
		generator = UtilsProviders.provide_generator()
		generator.generate(
			QueryParams(
				lyrics=[""]
			)
		)

	def test_raw_functionality(self):
		generator = UtilsProviders.provide_generator()
		generator.generate(

		)
