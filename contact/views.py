from django.shortcuts import render
from django.views import generic
from .models import Me, Contact
from .forms import ContactForm


class IndexView(generic.TemplateView):
    template_name = "contact/me.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['me'] = Me.objects.get()
        context['form'] = ContactForm
        return context


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            post = form.save(commit=False)
            post.save()
            context = {'name': data['name'],}
            return render(request, 'contact/success.html',context)
    else:
        form = ContactForm()
    return render(request, 'contact/contactform.html',{'form':form})
