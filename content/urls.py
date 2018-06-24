from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^check_answer/$', views.check_answer, name='check_answer')
]
