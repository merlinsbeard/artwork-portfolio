from django.shortcuts import render
from django.views import generic
from .models import Work, WorkTechnology
from contact.forms import ContactForm
from contact.models import Me
from .serializers import WorkSerializer 
from rest_framework import viewsets
from rest_framework import permissions

class IndexView(generic.ListView):

    def get_queryset(self):
        return Work.objects.filter(hidden=False)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['form'] = ContactForm()
        try:
            context['me'] = Me.objects.get()
        except:
            context['me'] = ''
        return context


class WorkDetailView(generic.DetailView):
    model = Work

class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes=[permissions.IsAdminUser]

