from rest_framework import serializers
from .models import Work


class WorkSerializer(serializers.HyperlinkedModelSerializer):
    techs = serializers.StringRelatedField(many=True)

    class Meta:
        model = Work
        fields = ('name', 'link', 'image', 'techs')
