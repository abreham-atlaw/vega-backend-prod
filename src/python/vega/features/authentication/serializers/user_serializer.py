
from rest_framework import serializers

from features.authentication.models import VegaUser


class VegaUserSerializer(serializers.ModelSerializer):

	class Meta:
		model = VegaUser
		fields = ["email", "full_name", "is_verified"]
