from rest_framework import serializers
from .models import Me


class MeSerializer(serializers.ModelSerializer):
    long_description_html = serializers.ReadOnlyField()
    class Meta:
        model = Me
        fields = (
            'user',
            'short_description',
            'long_description',
            'long_description_html',
            'image',
            'phone',
            'slug'
        )