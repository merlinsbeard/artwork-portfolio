from django.contrib.auth.models import User
from rest_framework import serializers
from works.models import Work, WorkImage
import logging

logger = logging.getLogger(__name__)


class WorkImageSerializer(serializers.ModelSerializer):
    # image = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = WorkImage
        fields = (
            'pk',
            'image',
            'description'
        )

    def get_image(self, obj):
        return f"{obj.image_append}"


class WorkSerializer(serializers.HyperlinkedModelSerializer):
    techs = serializers.StringRelatedField(many=True, read_only=True)
    image = serializers.SerializerMethodField()
    images = WorkImageSerializer(many=True)
    class Meta:
        model = Work
        fields = ('pk','slug', 'name','link','image',
                'description','short_description', 'techs', 'images')

    def get_image(self, obj):
        return f"{obj.image_append}"
