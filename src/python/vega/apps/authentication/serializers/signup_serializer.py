
from rest_framework import serializers

from apps.authentication.models import VegaUser


class SignupSerializer(serializers.Serializer):

	full_name = serializers.CharField()
	username = serializers.EmailField()
	password = serializers.CharField(min_length=8)

	def create(self, validated_data) -> VegaUser:
		user = VegaUser.objects.create_user(
			full_name=validated_data["full_name"],
			email=validated_data["username"],
			password=validated_data["password"]
		)
		return user
