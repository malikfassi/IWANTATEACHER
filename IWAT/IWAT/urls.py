from django.conf.urls import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^login/$', 'login.views.login'),
    (r'^admin/', include(admin.site.urls)),
    (r'^index/', 'annonces.views.getLastAnnouncement'),
    (r'^nouvelleAnnonce/', 'annonces.views.postAnnonce'),
    (r'^signin/', "login.views.signin"),
    (r'^home/', "login.views.home"),
	(r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/home/'})
    #ajouter page signin
)
