"""neighbourhood URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django_registration.backends.one_step.urls import views as v
from django.contrib.auth import views, logout as auth_logout, login as auth_login
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf import settings
from django.views.static import serve
# RestAPI authentication
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('neighbors.urls')),
    # Accounts
    url(r'^accounts/', include('django_registration.backends.one_step.urls')),
    # url(r'^accounts/login/$', v.login, {"next_page": '/'}),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    # Favicon
    # path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
    # Static fixes
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    # RestAPI Authentication
    url(r'^api-token-auth/', obtain_auth_token)
]