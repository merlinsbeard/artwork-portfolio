from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(
            widget=forms.TextInput(attrs={'class':'validate'}))
    message = forms.CharField(
            widget=forms.Textarea(
                attrs={'class':'materialize-textarea'}))
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')

    def send_mail(self):
        message = """
                Name: {},
                email: {},
                Message: {}
                date_added: {}
                """.format(self.name, self.email,
                        self.message, self.date_added)
        pass
