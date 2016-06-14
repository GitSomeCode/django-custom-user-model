from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^success_register/$', views.success_register, name='success_register'),
    url(r'^success_login/$', views.success_login, name='success_login')
]
