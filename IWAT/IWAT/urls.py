from django.conf.urls import *
from login.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^login/$', 'login.views.login_user'),
    (r'^admin/', include(admin.site.urls)),
    (r'^index/', 'annonces.views.getLastAnnouncement'),
    (r'^nouvelleAnnonce/', 'annonces.views.postAnnonce'),
    #ajouter page signin
)
