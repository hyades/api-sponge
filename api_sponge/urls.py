from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'api_sponge.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^testget/?$', views.test_get),
    url(r'^testpost/?$', views.test_post),
)
