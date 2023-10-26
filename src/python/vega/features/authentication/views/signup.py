from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from features.authentication.serializers import VegaUserSerializer, SignupSerializer


class SignupView(APIView):

    def post(self, request):
        serializer = SignupSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        response_serializer = VegaUserSerializer(instance=user)
        return Response(
            data=response_serializer.data,
            status=status.HTTP_201_CREATED
        )
