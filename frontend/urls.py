from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^info/$', views.info_choice, name='info_choice'),
    url(r'^info/(?P<type_variable>\w+)/$', views.info, name='info'),
    url(r'^test/$', views.test_choice_group, name='test_choice_group'),
    url(r'^test/(?P<element_group>\w+)/$', views.test_choice_type, name='test_choice_type'),
    url(r'^test/(?P<element_group>\w+)/(?P<element_type>\w+)/(?P<element_id>\w+)/$', views.test, name='test'),
    url(r'^stat/(?P<element_group>\w+)/(?P<element_type>\w+)/$', views.stat, name='stat'),
]
