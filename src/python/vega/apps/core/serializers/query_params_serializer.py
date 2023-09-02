
from rest_framework import serializers

from rest_framework import serializers

from apps.core.models import QueryParams, Lyrics, Instrumental

from rest_framework import serializers


class QueryParamsSerializer(serializers.Serializer):

    genre = serializers.CharField(max_length=255, allow_blank=True)
    era = serializers.CharField(max_length=255, allow_blank=True)
    lyrics = serializers.ListField(child=serializers.CharField(), allow_null=True)
    instruments = serializers.ListField(child=serializers.CharField(), allow_null=True)

    def create(self, validated_data) -> QueryParams:

        query_params = QueryParams(
            genre=validated_data.get('genre'),
            era=validated_data.get('era'),
            mood=validated_data.get("mood")
        )
        query_params.save()
        lyrics = [
            Lyrics(
                value=lyrics,
                query_params=query_params
            )
            for lyrics in validated_data.get("lyrics", [])
        ]
        instruments = [
            Instrumental(
                value=instrument,
                query_params=query_params
            )
            for instrument in validated_data.get("instruments", [])
        ]

        for foreign in lyrics + instruments:
            foreign.save()



        return query_params
