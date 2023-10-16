
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.core.models import GenerationRequest, QueryParams
from apps.core.serializers.generation_request_serializer import GenerationRequestSerializer
from apps.core.serializers.query_params_sample_serializer import QueryParamsSampleSerializer
from apps.core.serializers.query_params_serializer import QueryParamsSerializer
from di.utils_providers import UtilsProviders
from utils.generator import GenerationThread


class GenerateView(APIView):

	# permission_classes = [IsAuthenticated]

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.__generator = UtilsProviders.provide_generator()

	def __start_generation(self, query_params: QueryParams, request: GenerationRequest):
		thread = GenerationThread(
			query_params=query_params,
			request=request,
			generator=self.__generator
		)
		thread.start()

	def post(self, request: Request) -> Response:
		generation_request: GenerationRequest = GenerationRequest.objects.create()

		serializer = QueryParamsSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		query_params = serializer.create(serializer.validated_data)

		self.__start_generation(query_params, generation_request)

		return Response({
			"request_id": generation_request.id
		})


class GenerationStatusView(APIView):

	# permission_classes = [IsAuthenticated]

	def get(self, request: Request):
		request_id = request.query_params.get('id')
		generation_request = get_object_or_404(GenerationRequest, id=request_id)

		serializer = GenerationRequestSerializer(instance=generation_request)
		return Response(
			serializer.data
		)


class RecommendationsView(APIView):

	permission_classes = [IsAuthenticated]

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.__recommender = UtilsProviders.provide_recommender()

	def get(self, request: Request) -> Response:
		params = self.__recommender.recommend(request.user)
		serializer = QueryParamsSampleSerializer(instance=params, many=True)
		return Response(
			serializer.data
		)