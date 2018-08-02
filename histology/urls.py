from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^histology/check/$', views.histology_check, name='histology_check'),
    url(r'^histology/stat/(?P<element_type>\w+)/$', views.histology_stat, name='histology_stat'),
    url(r'^histology/$', views.histology_choice_type, name='histology_choice_type'),
    url(r'^histology/(?P<element_type>\w+)/(?P<element_id>\w+)/$', views.histology, name='histology')
]
