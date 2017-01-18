from django.shortcuts import render
from django.views import generic
from .models import Work


class IndexView(generic.ListView):

    def get_queryset(self):
        return Work.objects.filter(hidden=False)


class WorkDetailView(generic.DetailView):
    model = Work
