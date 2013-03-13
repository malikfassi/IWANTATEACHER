from django.forms import ModelForm

from cours.models import CourEvenement, CourCompetence, CourCompetenceUser

class ContexteForm(ModelForm):
	class Meta:
		model = CourEvenement
		exclude = ('sujet', 'eleve')

class CourCompetenceForm(ModelForm):
    class Meta:
        model = CourCompetence

class CourCompetenceUserForm(ModelForm):
    class Meta:
        model = CourCompetenceUser