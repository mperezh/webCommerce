from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', view=views.index, name='home'),
    url(r'^home/$', view=views.index, name='home'),
]
