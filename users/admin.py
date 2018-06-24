from django.contrib import admin
from .models import *


class UserInfoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserInfo._meta.fields]

    class Meta:
        model = UserInfo


admin.site.register(UserInfo, UserInfoAdmin)
