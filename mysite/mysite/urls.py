"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from rest.views import QuestionViewSet
from rest.views import AnswerViewSet
# from rest.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'answer', AnswerViewSet)
# router.register(r'user', UserViewSet)


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'rest.views.hello_world'),
    url(r'^async/', 'rest.views.hello_async'),
    url(r'^api/', include(router.urls)),
]
