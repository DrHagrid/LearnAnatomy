from django.contrib import admin
from .models import *


class BoneTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BoneType._meta.fields]

    class Meta:
        model = BoneType


class BoneAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Bone._meta.fields]

    class Meta:
        model = Bone


class MuscleTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MuscleType._meta.fields]

    class Meta:
        model = MuscleType


class MuscleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Muscle._meta.fields]

    class Meta:
        model = Muscle


admin.site.register(BoneType, BoneTypeAdmin)
admin.site.register(Bone, BoneAdmin)

admin.site.register(MuscleType, MuscleTypeAdmin)
admin.site.register(Muscle, MuscleAdmin)
