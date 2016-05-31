from django.contrib.auth import get_user_model
from rest_framework import serializers

from seresults.models import SearchRequest, search_engine_options, status_options


class UserSerializer(serializers.Serializer):
    def create(self, validated_data):
        return get_user_model().objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.username
        instance.email = validated_data.email
        instance.first_name = validated_data.first_name
        instance.last_name = validated_data.last_name
        instance.save()
        return instance

    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)


class SearchRequestSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    search_engine = serializers.ChoiceField(choices=search_engine_options())
    status = serializers.ChoiceField(choices=status_options())

    class Meta:
        model = SearchRequest
        fields = ('query', 'search_engine', 'search_engine_name', 'status',
                  'status_name', 'user', 'username', 'results')
