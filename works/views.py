from django.shortcuts import render
from django.views import generic
from .models import Work, WorkTechnology
from contact.forms import ContactForm
from contact.models import Me
from .serializers import WorkSerializer, WorkTechSerializer
from rest_framework import viewsets

class IndexView(generic.ListView):

    def get_queryset(self):
        return Work.objects.filter(hidden=False)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['form'] = ContactForm()
        context['me'] = Me.objects.get()
        return context


class WorkDetailView(generic.DetailView):
    model = Work

class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

class WorkTechViewSet(viewsets.ModelViewSet):
    queryset = WorkTechnology.objects.all()
    serializer_class = WorkTechSerializer
