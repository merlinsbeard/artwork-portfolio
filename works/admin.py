from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Work, WorkImage, WorkTechnology
from django.forms import Textarea
from django.db import models


def mini_textfield():
    formfield_overrides={
            models.TextField: {'widget': Textarea(
                attrs={'rows':2,
                        'cols':40,})},
                }
    return formfield_overrides


class WorkImageInstanceInline(admin.TabularInline):
    model = WorkImage
    extra = 1
    formfield_overrides = mini_textfield()


class WorkTechInstanceInline(admin.TabularInline):
    model = WorkTechnology
    extra = 1
    formfield_overrides = mini_textfield()


class WorkAdmin(admin.ModelAdmin):
    inlines = [WorkImageInstanceInline, WorkTechInstanceInline]
    #readonly_fields = ("show_url",)
    formfield_overrides = mini_textfield()

    def show_url(self, instance):
        url = reverse("work:detail",
                kwargs={"slug":instance.slug})
        response = format_html("""<a href="{0}">{1}</a>""", url, url)
        return response
    
    def show_image(self, instance):
        response = format_html("""<img src="{1}"/>""", instance.image)
        return response


    #show_url.allow_tags = True

admin.site.register(Work, WorkAdmin)
admin.site.register(WorkImage)
