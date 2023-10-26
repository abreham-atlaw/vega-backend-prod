from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from features.core.models import GenerationRequest, QueryParams
from features.core.serializers import QueryParamsSerializer


class GenerateViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = "/api/core/song/generate"

    def test_generate_view(self):
        generation_request = GenerationRequest.objects.create()
        query_params = QueryParams.objects.create(genre='pop', era='2000s', mood='happy')

        serializer = QueryParamsSerializer(query_params)

        response = self.client.post(self.url, serializer.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data, {"request_id": str(generation_request.id)})
