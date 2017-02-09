#from django.shortcuts import render
from django.views import generic
from .models import Work
from contact.forms import ContactForm
from contact.models import Me
from .serializers import WorkSerializer
from rest_framework import viewsets
from rest_framework import permissions
from .forms import WorkForm, TechInlineFormSet
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(generic.ListView):

    def get_queryset(self):
        return Work.objects.filter(hidden=False)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['form'] = ContactForm()
        try:
            context['me'] = Me.objects.get(slug='me')
        except:
            context['me'] = ''
        return context


class WorkDetailView(generic.DetailView):
    model = Work


class WorkUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Work
    form_class = WorkForm
    #fields = ('name','short_description', 'description',
    #        'slug','link','image','hidden', 'work.images')


class WorkCreateView(LoginRequiredMixin, generic.CreateView):
    model = Work
    form_class = WorkForm
    template_name = 'works/work_create.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        tech_form = TechInlineFormSet()
        return self.render_to_response(
                        self.get_context_data(
                            form=form, tech_form=tech_form))


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [permissions.IsAdminUser]
