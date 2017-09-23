"""TestHelper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from answers.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^group/(?P<group_id>[0-9]+)', answers), #просмотр списка вопросов определенной группы
    url(r'^group/question_id=(?P<question_id>[0-9]+)', question_id), #просмотр списка вопросов определенной группы
    url(r'^', list), #список групп вопросов
]
