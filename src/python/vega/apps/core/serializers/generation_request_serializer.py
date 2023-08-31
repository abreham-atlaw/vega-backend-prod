
from rest_framework import serializers

from apps.core.models import GenerationRequest


class GenerationRequestSerializer(serializers.ModelSerializer):

	class Meta:
		model = GenerationRequest
		fields = ["song", "status"]
