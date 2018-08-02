from django.contrib import admin
from .models import *


class SampleTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']

    class Meta:
        model = SampleType


class SampleAdmin(admin.ModelAdmin):
    list_display = ['id', 'correct_option']
    list_display_links = ['id', 'correct_option']

    class Meta:
        model = Sample


admin.site.register(SampleType, SampleTypeAdmin)
admin.site.register(Sample, SampleAdmin)
