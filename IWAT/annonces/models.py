from django.db import models
from cours.models import CourEvenement
from cours.models import CourEvenementForm
from login.models import Utilisateur, UtilisateurForm
import django.forms

class Annonce(models.Model):
    contexte = models.OneToOneField(CourEvenement, related_name="contexteInAnnonce")
    postePar = models.OneToOneField(Utilisateur, related_name="posteurInAnnonce")
    posteLe = models.DateTimeField()

    def __unicode__(self):
        return (self.posterPar.__unicode__()+ " cherche un cour de " + self.contexte.__unicode__())

    def __repr__(self):
        return self.__unicode__()

class AnnonceForm(CourEvenementForm, UtilisateurForm):
    pass
 
class Notification(models.Model):
    emetteur = models.ForeignKey(Utilisateur, related_name="emetteurInNotification")
    recepteur = models.ForeignKey(Utilisateur, related_name="recepteurInNotification")
    message = models.CharField(max_length=750)
    vu = models.BooleanField()

    def __unicode__(self):
        return self.message

    def __repr__(self):
        return self.__unicode__()