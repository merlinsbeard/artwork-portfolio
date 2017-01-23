from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
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
