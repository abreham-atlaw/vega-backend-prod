import typing

from django.contrib.auth.models import User

from apps.core.models import QueryParamsSample, Lyrics, Instrumental
from utils.recommendation.query_recommender import QueryRecommender


"""
id = models.UUIDField(primary_key=True, default=uuid.uuid4)
genre = models.CharField(max_length=255, null=True)
era = models.CharField(max_length=255, null=True)
mood = models.CharField(max_length=255, null=True)

"""
"""
class Lyrics(models.Model):
	value = models.CharField(max_length=255)
	query_params = models.ForeignKey(QueryParams, on_delete=models.CASCADE)


class Instrumental(models.Model):
	value = models.CharField(max_length=255)
	query_params = models.ForeignKey(QueryParams, on_delete=models.CASCADE)



"""


class MockQueryRecommender(QueryRecommender):

	def __create_params(self, user: User) -> QueryParamsSample:
		params = QueryParamsSample.objects.create(
			title="Late Night Drive",
			cover="https://www.dropbox.com/scl/fi/drccrseeclv9sht0kv4h9/_c7667c25-ac02-4f86-a9ac-ef38895ddf76.jpeg?rlkey=smukn5hw3et6267bdb4wwjsef&dl=0&raw=1",
			genre="Hip Hop",
			era="Modern",
			mood="Happy"
		)

		lyrics = ["descriptive", "poetic"]
		instruments = ["piano", "drums"]

		for lyric in lyrics:
			Lyrics.objects.create(
				value=lyric,
				query_params=params
			)

		for instrument in instruments:
			Instrumental.objects.create(
				value=instrument,
				query_params=params
			)

		return params

	def recommend(self, user: User) -> typing.List[QueryParamsSample]:
		return [
			self.__create_params(user)
		]
