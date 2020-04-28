"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from . import view, testdb, search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', view.hello),
    url(r'^$', view.index),
    url(r'^hello$', view.hello),
    # url(r'^initu$', testdb.init_user),
    url(r'^getu$', testdb.get_user),
    # url(r'^initc$', testdb.init_car),
    url(r'^getc$', testdb.get_car),
    # url(r'^initt$', testdb.init_task),
    url(r'^gett$', testdb.get_task),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^login', view.login),
    url(r'.*', view.notfound)
]
