from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate


class LoginView(APIView):

	def post(self, request: Request):
		username = request.data.get('username')
		password = request.data.get('password')

		user = authenticate(request, username=username, password=password)
		if user:
			token, created = Token.objects.get_or_create(user=user)
			return Response({
				'token': token.key
			})
		else:
			return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
