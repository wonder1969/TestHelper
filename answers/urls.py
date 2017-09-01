from django.conf.urls import include, url
from answers.views import list

urlpatterns = [
    url(r'^$', list, name='list'),
]