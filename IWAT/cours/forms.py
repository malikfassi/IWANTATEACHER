from django.forms import ModelForm
from django import forms

from cours.models import *
class ContexteForm(ModelForm):
	class Meta:
		model = CourEvenement
		exclude = ('sujet', 'eleve', "prof")

class CourCompetenceForm(forms.Form):
	secteur =forms.CharField(max_length="2",  widget=forms.Select(choices=Matieres))
	anneeSecteur = forms.CharField(max_length="2", widget=forms.Select(choices=AnneeEtude))

class CourCompetenceUserForm(ModelForm):
    class Meta:
        model = CourCompetenceUser