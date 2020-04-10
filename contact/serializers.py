from rest_framework import serializers
from .models import Me


class MeSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField()
    email = serializers.ReadOnlyField()
    long_description_html = serializers.ReadOnlyField()
    class Meta:
        model = Me
        fields = (
            'name',
            'email',
            'user',
            'short_description',
            'long_description',
            'long_description_html',
            'image',
            'phone',
            'slug'
        )