"""qzzzme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.urls import path
from graphene_django.views import GraphQLView
from django.contrib.auth import views as auth_views

from qzzzme_app.views import FacebookLogin

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^rest-auth/', include('rest_auth.urls')) ,
    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1.0/',
        include("qzzzme_app.urls", namespace="qzzzme_app-api")),
    path("graphql/", GraphQLView.as_view(graphiql=True))
]
