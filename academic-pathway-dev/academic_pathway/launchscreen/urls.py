"""LaunchScreen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.initial_view, name='initial_view'),
    url(r'submit_initial_input/$', views.submit_initial_input, name='submit_initial_input'),
    url(r'gre_search/$', views.gre_search, name='gre_search'),
    url(r'major_detail/(?P<m_id>[0-9]+)$', views.major_detail, name='major_detail'),

]
