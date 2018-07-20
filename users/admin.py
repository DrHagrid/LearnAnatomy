from django.contrib import admin
from .models import *


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    list_display_links = ['id', 'user']
    #readonly_fields = ['data', ]

    class Meta:
        model = UserInfo


admin.site.register(UserInfo, UserInfoAdmin)
