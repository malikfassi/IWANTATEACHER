from django.contrib import admin
from cours.models import CourCompetence, CourEvenement, CourCompetenceUser

admin.site.register(CourCompetence)
admin.site.register(CourEvenement)
admin.site.register(CourCompetenceUser)