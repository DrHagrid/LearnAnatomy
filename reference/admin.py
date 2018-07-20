from django.contrib import admin
from .models import *


class ArticleSectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'variable']
    list_display_links = ['id', 'name']

    class Meta:
        model = ArticleSection


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'section', 'date', 'is_active']
    list_display_links = ['id', 'title']
    list_editable = ['is_active', ]

    class Meta:
        model = Article


class PictureAdmin(admin.ModelAdmin):
    list_display = ['id', 'code']
    list_display_links = ['id', ]
    readonly_fields = ['code', ]

    class Meta:
        model = Picture


admin.site.register(ArticleSection, ArticleSectionAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Picture, PictureAdmin)
