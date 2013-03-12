from django.db import models
from django.contrib.auth.models import User
from django import forms

class Utilisateur(models.Model):
	profilBase = models.OneToOneField(User, primary_key=True, related_name='profilBaseInUtilisateur')
	dateNaissance = models.DateField()
	#afsbreljked= models.CharField(max_length=7)
	#competences -> many-to-one-> utilisateur
    #historique(cours) -> many-to-one -> utilisateur
	#notification -> many-to-one -> utilisateur

	def __unicode__(self):
		return (self.profilBase.first_name+" "+self.profilBase.last_name+" @ "+self.profilBase.email)

	def __repr__(self):
		return self.__unicode__()

class LoginForm(forms.Form):
	pseudo = forms.CharField(max_length=75)
	mdp = forms.CharField(max_length=75)

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		exclude = ("groups", "user_permission", "is_active", "is_superuser", "last_login", "date_joined")

class UtilisateurForm(UserForm):
	dateNaissanceField = forms.DateField()

class SignInForm(forms.ModelForm):
	class meta:
		model = User
		exlude = ("profilBase", "dateNaissance")