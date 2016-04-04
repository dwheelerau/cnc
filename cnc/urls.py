"""cnc URL Configuration

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
from concordianbc import views as concordianbc_views
# from concordianbc import urls as concordianbc_urls

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', concordianbc_views.home_page, name='home'),
    url(r'^results/', concordianbc_views.results_page, name='results'),
    url(r'^about/', concordianbc_views.about_page, name='about'),
    # url(r'^concordianbc/', include(concordianbc_urls)),
    # url(r'^$', include(concordianbc_urls)),
]
