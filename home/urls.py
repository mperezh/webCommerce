from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', view=views.index, name='home'),
    url(r'^home/$', view=views.index, name='home'),
    url(r'^about/$', view=views.about, name='about'),
    url(r'^search/$', view=views.search, name='search'),
    url(r'^contact/$', view=views.contact, name='contact'),
]