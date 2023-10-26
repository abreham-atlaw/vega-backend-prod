from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from features.authentication.models import VegaUser
from features.authentication.serializers import VegaUserSerializer


class UserExistsView(APIView):

	def get(self, request: Request):
		exists = VegaUser.objects.filter(email=request.query_params.get("email")).exists()
		return Response({
			"exists": exists
		})


class WhoAmIView(APIView):

	permission_classes = [IsAuthenticated]

	def get(self, request: Request):
		serializer = VegaUserSerializer(instance=request.user)
		return Response(serializer.data)
