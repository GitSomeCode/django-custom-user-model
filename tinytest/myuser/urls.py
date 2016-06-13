from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.custom_login, name='custom_login'),
    url(r'^logout/$', views.custom_logout, name='custom_logout'),
    url(r'^register/$', views.register, name='register'),
]
