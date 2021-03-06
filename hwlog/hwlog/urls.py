"""hwlog URL Configuration

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
from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from log import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    path('', include('django.contrib.auth.urls')),
    #url(r'^login/$', auth_views.login, name = 'login'),
    #url(r'^logout/$', auth_views.logout,{'next_page': '/'}, name = 'logout'),
    url(r'^signup/$', views.signup, name= 'signup'),
    url(r'^password/$', views.change_password, name='change_password'),
    url(r'^configure/$', views.configure, name = 'configure'),
    url(r'^log/', include('log.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^about/', views.about, name = 'about'),
    url(r'^pong/', views.game, name = 'game'),
    url(r'^martor/', include('martor.urls')),
]
