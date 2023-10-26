import typing

from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from features.core.models import GenerationRequest, QueryParams
from features.core.serializers.generation_request_serializer import GenerationRequestSerializer
from features.core.serializers.query_params_sample_serializer import QueryParamsSampleSerializer
from features.core.serializers.query_params_serializer import QueryParamsSerializer
from dependency_injection.utils_providers import UtilsProviders
from utils.generator import GenerationThread


class GenerateView(APIView):

	# Only authenticated users can access this view
	permission_classes = [IsAuthenticated]

	# Initialize the GenerateView object and provide a generator
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.__generator = UtilsProviders.provide_generator()

	# Private method to start a new generation thread
	def _start_generation(self, request: GenerationRequest, query_params: typing.Optional[QueryParams] = None, raw_query: typing.Optional[str] = None):
		# Create a new GenerationThread object and start it
		thread = GenerationThread(
			query_params=query_params,
			request=request,
			raw_query=raw_query,
			generator=self.__generator
		)
		thread.start()

	# Handle POST requests to this view
	def post(self, request: Request) -> Response:
		# Create a new GenerationRequest object
		generation_request: GenerationRequest = GenerationRequest.objects.create()

		# Validate the request data and create a QueryParams object from it
		serializer = QueryParamsSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		query_params = serializer.create(serializer.validated_data)

		# Start a new generation thread with the request and query parameters
		self._start_generation(generation_request, query_params=query_params)

		# Return a response with the ID of the generation request
		return Response({
			"request_id": generation_request.id
		})


class RawGenerateView(GenerateView):

	# Only authenticated users can access this view
	permission_classes = [IsAuthenticated]

	# Handle POST requests to this view
	def post(self, request: Request) -> Response:
		# Create a new GenerationRequest object
		generation_request: GenerationRequest = GenerationRequest.objects.create()

		# Get the raw query from the request data
		query = request.data.get("query")
		# If the query is not provided, return a 400 response
		if query is None:
			return Response("{query: This field is required}", status=400)

		# Start a new generation thread with the request and raw query
		self._start_generation(
			generation_request,
			raw_query=query
		)

		# Return a response with the ID of the generation request
		return Response({
			"request_id": generation_request.id
		})


# A View to check on the status of the generation.
class GenerationStatusView(APIView):

	permission_classes = [IsAuthenticated]

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