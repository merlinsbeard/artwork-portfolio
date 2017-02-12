#from django.shortcuts import render
from django.views import generic
from .models import Work, WorkTechnology
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

    def get_object(self, queryset=None):
        instance = Work.objects.get(slug=self.kwargs.get('slug',''))
        return instance 

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        techs = WorkTechnology.objects.filter(work=self.object)
        tech_form = TechInlineFormSet(instance=self.object)
        return self.render_to_response(
                self.get_context_data(form=form, tech_form=tech_form)
                )
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        tech_form = TechInlineFormSet(self.request.POST, instance=self.object)
        if form.is_valid() and tech_form.is_valid():
            return self.form_valid(form, tech_form)
        else:
            pass
            #return self.form_invalid(form, tech_form)

    def form_valid(self, form, tech_form):
        form.save()
        tech_form.save()



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
