"""SiteV2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

from AskcarlApp import views, auth # plus tard rajouter forms et auth




urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/', auth.login, name = 'login'),
	url(r'^logout/', auth.logout, name = 'logout'),
	url(r'^register/', auth.register, name = 'register'),
	url(r'^about/', views.about, name='about'),
	url(r'^blog/', views.blog, name='blog'),
	url(r'^datawarehouse_registered/', views.datawarehouse_registered, name='datawarehouse_registered'),
	url(r'^datawarehouse_unregistered/', views.datawarehouse_unregistered, name='datawarehouse_unregistered'),
	url(r'^pricing/', views.pricing, name='pricing'),
    url(r'^admin/', admin.site.urls),
]
