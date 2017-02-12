from django import forms
from .models import Work, WorkTechnology, WorkImage


class WorkForm(forms.ModelForm):
    description = forms.CharField(
            widget=forms.Textarea(
                attrs={'class': 'materialize-textarea'}))

    class Meta:

        model = Work
        fields = [
                'name', 'short_description', 'description',
                'slug', 'link', 'image', 
                ]

class TechForm(forms.ModelForm):
    class Meta:
        model = WorkTechnology
        fields=('name',)


TechInlineFormSet = forms.inlineformset_factory(
        Work, WorkTechnology,
        extra=1,
        fields=('name',)
        )

class ImageForm(forms.ModelForm):
    description = forms.CharField(
            widget=forms.Textarea(
                attrs={'class': 'materialize-textarea'}))
    class Meta:
        model = WorkImage
        fields=('image', 'description')

ImageInlineFormSet = forms.inlineformset_factory(
        Work, WorkImage,
        extra=2,
        form=ImageForm,
        #fields= ('image', 'description')
        )

