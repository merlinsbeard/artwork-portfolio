from django.shortcuts import render
from rest_framework import viewsets
from works.models import Work
from .serializers import WorkSerializer


class WorkViewSet(viewsets.ModelViewSet):
    """
    API End pot
    """
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

