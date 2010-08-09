from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'artists.views.guitarrists', name='guitarrists'),
    url(r'^(?P<slug>[\w-]+)/$', 'artists.views.guitarrist', name='guitarrists'),
)
