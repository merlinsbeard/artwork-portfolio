from django.shortcuts import render
from django.views import generic
from .models import Me
from .forms import ContactForm, MeForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
import os


class IndexView(generic.TemplateView):
    template_name = "contact/me.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        try:
            context['me'] = Me.objects.get(slug='me')
        except:
            context['me'] = ''
        context['form'] = ContactForm
        return context


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            post = form.save(commit=False)
            post.save()
            contact_me_mail(data['name'], data['email'], data['message'])
            context = {'name': data['name'], }
            return render(request, 'contact/success.html', context)
    else:
        form = ContactForm()
    return render(request, 'contact/contactform.html', {'form': form})


# REMOVE THIS when sendmail is done in models.py
def contact_me_mail(from_person, from_email, message):
    # Formated email
    subject = "New Contact from {}".format(from_person)
    message = """
            from: {}
            email: {}
            message: {}
            """.format(from_person, from_email, message)

    to = os.environ['EMAIL_TO']
    from_ = os.environ['EMAIL_HOST_USER']
    send_mail(subject, message, from_, [to], fail_silently=False)


class MeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Me
    form_class = MeForm
    template_name = 'contact/me_update.html'

    def get_success_url(self):
        return reverse('contact:me')

    def get_object(self, queryset=None):
        return self.request.user.me
        #return self.request.user

