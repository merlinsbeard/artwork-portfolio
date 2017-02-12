from django import forms
from .models import Contact, Me
from django.contrib.auth.models import User



class ContactForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'validate'}))
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'materialize-textarea'}))


    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')

    def send_mail(self):
        message = """
                Name: {},
                email: {},
                Message: {}
                date_added: {}
                """.format(
                        self.name, self.email,
                        self.message, self.date_added)
        pass


class MeForm(forms.ModelForm):
    long_description = forms.CharField(
        widget=forms.Textarea(
                attrs={'class': 'materialize-textarea'}))
    first_name = forms.CharField(max_length=256)


    class Meta:
        model = Me
        fields = ['slug', 'short_description', 'long_description', 'phone', 'image']

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

MeFormSet = forms.inlineformset_factory(User, Me, form=MeForm)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email' ]
