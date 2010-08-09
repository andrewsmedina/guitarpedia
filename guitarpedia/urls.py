from django.conf.urls.defaults import *

urlpatterns = patterns('',

    url(r'^$', 'home.views.index', name='index'),

    (r'^guitarrists/', include('artists.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
