from rest_framework import serializers
from .models import Work, WorkTechnology


class WorkSerializer(serializers.HyperlinkedModelSerializer):
    techs = serializers.StringRelatedField(many=True)
    class Meta:
        model = Work
        fields = ('name','link','image', 'techs') 

class WorkTechSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkTechnology
        fields = ('name','work')
