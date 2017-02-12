#from django.shortcuts import render
from django.views import generic
from .models import Work, WorkTechnology, WorkImage
from contact.forms import ContactForm
from contact.models import Me
from .serializers import WorkSerializer
from rest_framework import viewsets
from rest_framework import permissions
from .forms import WorkForm, TechInlineFormSet, ImageInlineFormSet
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse


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
        images = WorkImage.objects.filter(name=self.object)
        tech_form = TechInlineFormSet(instance=self.object)
        image_form = ImageInlineFormSet(instance=self.object)
        return self.render_to_response(
                self.get_context_data(form=form, tech_form=tech_form,
                    image_form=image_form)
                )
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        tech_form = TechInlineFormSet(self.request.POST, instance=self.object)
        image_form = ImageInlineFormSet(self.request.POST, instance=self.object)
        if form.is_valid() and tech_form.is_valid() and image_form.is_valid():
            return self.form_valid(form, tech_form, image_form)
        else:
            pass
            #return self.form_invalid(form, tech_form)

    def form_valid(self, form, tech_form, image_form):
        form.save()
        tech_form.save()
        image_form.save()
        return reverse('works:list')



class WorkCreateView(LoginRequiredMixin, generic.CreateView):
    model = Work
    form_class = WorkForm
    template_name = 'works/work_create.html'


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [permissions.IsAdminUser]
