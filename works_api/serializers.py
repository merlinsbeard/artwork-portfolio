from django.contrib.auth.models import User
from rest_framework import serializers
from works.models import Work, WorkImage


class WorkImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = WorkImage
        fields = (
            'pk',
            'image',
            'description'
        )


class WorkSerializer(serializers.HyperlinkedModelSerializer):
    techs = serializers.StringRelatedField(many=True)
    image = serializers.ImageField(use_url=True)
    images = WorkImageSerializer(many=True)
    class Meta:
        model = Work
        fields = ('pk','slug', 'name','link','image',
                'description','short_description', 'techs', 'images')
