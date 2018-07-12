from django.contrib import admin
from .models import *


class ArticleSectionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ArticleSection._meta.fields]

    class Meta:
        model = ArticleSection


class ArticleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Article._meta.fields]

    class Meta:
        model = Article


admin.site.register(ArticleSection, ArticleSectionAdmin)
admin.site.register(Article, ArticleAdmin)
