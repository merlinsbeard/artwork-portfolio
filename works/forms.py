from django import forms
from .models import Work, WorkTechnology

class WorkForm(forms.ModelForm):
    description = forms.CharField(
            widget=forms.Textarea(
                attrs={'class':'materialize-textarea'}))
    class Meta:
        model = Work
        fields = ['name','short_description', 'description',
                'slug','link','image','hidden', ]


TechInlineFormSet = forms.inlineformset_factory(
        Work, WorkTechnology,
        extra=1,
        fields = ('name',)
        )
