from django.contrib import admin
from .models import *


class BoneTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'variable']
    list_display_links = ['id', 'name']

    class Meta:
        model = BoneType


class BoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_rus', 'name_lat', 'type', 'is_active']
    list_display_links = ['id', 'name_rus']
    list_editable = ['is_active', ]

    list_filter = ['type', ]
    search_fields = ['name_rus', 'name_lat']

    class Meta:
        model = Bone


class MuscleTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'variable']
    list_display_links = ['id', 'name']

    class Meta:
        model = MuscleType


class MuscleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_rus', 'name_lat', 'type', 'is_active']
    list_display_links = ['id', 'name_rus']
    list_editable = ['is_active', ]

    list_filter = ['type', ]
    search_fields = ['name_rus', 'name_lat']

    class Meta:
        model = Muscle


admin.site.register(BoneType, BoneTypeAdmin)
admin.site.register(Bone, BoneAdmin)

admin.site.register(MuscleType, MuscleTypeAdmin)
admin.site.register(Muscle, MuscleAdmin)
