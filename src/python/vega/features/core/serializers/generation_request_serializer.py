
from rest_framework import serializers

from features.core.models import GenerationRequest


class GenerationRequestSerializer(serializers.ModelSerializer):

	class Meta:
		model = GenerationRequest
		fields = ["song", "status"]
