from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^latin/check/$', views.latin_check, name='latin_check'),
    url(r'^latin/stat/(?P<element_group>\w+)/(?P<element_type>\w+)/$', views.latin_stat, name='latin_stat'),
    url(r'^latin/$', views.latin_choice_group, name='latin_choice_group'),
    url(r'^latin/(?P<element_group>\w+)/$', views.latin_choice_type, name='latin_choice_type'),
    url(r'^latin/(?P<element_group>\w+)/(?P<element_type>\w+)/(?P<element_id>\w+)/$', views.latin, name='latin'),
]
