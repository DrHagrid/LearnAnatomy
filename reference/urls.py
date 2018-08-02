from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^reference/$', views.reference_choice, name='reference_choice'),
    url(r'^reference/(?P<article_id>\w+)/$', views.reference, name='reference'),
    url(r'^about/$', views.about, name='about'),
]
