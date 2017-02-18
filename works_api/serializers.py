from django.contrib.auth.models import User
from rest_framework import serializers
from works.models import Work

class WorkSerializer(serializers.HyperlinkedModelSerializer):
    techs = serializers.StringRelatedField(many=True)
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = Work
        fields = ('name','link','image',
                'description','short_description', 'techs')
