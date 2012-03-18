from django.conf.urls import patterns, include, url
from django.contrib import admin

from display.views import HomeView, JSONView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^data/$', JSONView.as_view(), name='data'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
