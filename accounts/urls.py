from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.profile, name='accounts.profile'),
    url(r'^login/$', views.loginView, name='accounts.login'),
    url(r'^logout/$', views.logoutView, name='accounts.logout'),
    url(r'^registration/$', views.registrationView, name='accounts.registration'),

]