from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^histology/check/$', views.histology_check, name='histology_check'),
    url(r'^histology/stat/$', views.histology_stat, name='histology_stat'),
    url(r'^histology/(?P<element_id>\w+)/$', views.histology, name='histology')
]
