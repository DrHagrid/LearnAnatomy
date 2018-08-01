from django.contrib import admin
from .models import *


class SampleAdmin(admin.ModelAdmin):
    list_display = ['id', 'correct_option']
    list_display_links = ['id', 'correct_option']

    class Meta:
        model = Sample


admin.site.register(Sample, SampleAdmin)
