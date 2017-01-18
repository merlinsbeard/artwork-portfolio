from django.contrib import admin
from .models import Work, WorkImage, WorkTechnology


class WorkImageInstanceInline(admin.TabularInline):
    model = WorkImage


class WorkTechInstanceInline(admin.TabularInline):
    model = WorkTechnology


class WorkAdmin(admin.ModelAdmin):
    inlines = [WorkImageInstanceInline, WorkTechInstanceInline]

admin.site.register(Work, WorkAdmin)
admin.site.register(WorkImage)
