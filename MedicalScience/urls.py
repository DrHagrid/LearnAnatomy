from django.contrib.auth.views import login, logout
from django.conf.urls import url, include
from django.contrib import admin
from users import views

urlpatterns = [
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
    url(r'^accounts/register/$', views.RegisterFormView.as_view(), name='register'),
    url(r'^admin/', admin.site.urls),
    url(r'', include('users.urls')),
    url(r'', include('reference.urls')),
    url(r'', include('latin.urls')),
    url(r'', include('histology.urls')),
]
