from rest_framework import serializers

from features.core.models import QueryParamsSample


class QueryParamsSampleSerializer(serializers.ModelSerializer):

	lyrics = serializers.ListField(child=serializers.CharField(), allow_null=True)
	instruments = serializers.ListField(child=serializers.CharField(), allow_null=True)

	class Meta:
		model = QueryParamsSample
		fields = "__all__"
