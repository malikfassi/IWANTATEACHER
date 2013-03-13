# -*- coding: cp1252 -*-
from django.db import models
from login.models import Utilisateur
from django.forms import ModelForm

Matieres = (
        #Langues
        ('FR', 'Langue Francaise'),
        ('EN', 'Langue Anglaise'),
        ('NL', 'Langue Néerlandaise'),
        #sciences
        ('SM', 'Science des Mathématiques'),
        ('SB', 'Science de la biologie'),
        ('SP', 'Science de la physique'),
        ('SC', 'Science de la chimie'),
        ('SG', 'Science humaine (géographie)'),
        ('SH', 'Science humaine (histoire)'),
        ('SP', 'Science humaine (philosophie)'),
        #litérature
        ('LF', 'Littérature Francaise'),
        ('LA', 'Littérature Anglaise'),
        ('LN', 'Littérature Néerlandaise'),
        #autres
        ('EC', 'Economie'),
        ('MO', 'Morale'),
        ('RE', 'Religion'),
    )

AnneeEtude = (
        #primaire
        ('P1', '1ére primaire'),
        ('P2', '2ére primaire'),
        ('P3', '3ére primaire'),
        ('P4', '4ére primaire'),
        ('P5', '5ére primaire'),
        ('P6', '6ére primaire'),
        #secondaire
        ('S1', '1ére secondaire'),
        ('S2', '2ére secondaire'),
        ('S3', '3ére secondaire'),
        ('S4', '4ére secondaire'),
        ('S5', '5ére secondaire'),
        ('S6', '6ére secondaire'),
        #supérieur
        ('B1', 'Bachelier 1ére'),
        ('B3', 'Bachelier 3ére'),
        ('B2', 'Bachelier 2ére'),
        ('M1', 'Master 1ére'),
        ('M2', 'Master 2ére'),
    )

class CourCompetence(models.Model):
    secteur = models.CharField(max_length="2", choices=Matieres)
    anneeSecteur = models.CharField(max_length="2", choices=AnneeEtude)

    def __unicode__(self):
        return( self.secteur+self.anneeSecteur)

    def __repr__(self):
        return (self.__unicode__())



class CourEvenement(models.Model):
    sujet = models.ForeignKey(CourCompetence, related_name="Cours(evenement)")
    heure = models.DateTimeField()
    lieu = models.CharField(max_length=200)
    eleve = models.ForeignKey(Utilisateur, related_name="eleve-in-Cour")
    prof = models.ForeignKey(Utilisateur, related_name="prof-in-Cour")
    
    def __unicode__(self):
        #return("Cours de "+ self.secteur+" "+self.anneeSecteur)
        return("Eleve : "+self.eleve.__repr__()+ " Professeur : " + self.prof.__repr__() + " à " + self.lieu)

    def __repr__(self):
        return( self.__unicode__())




class CourCompetenceUser(CourCompetence):            # |
    #courcompetenceuser -> many-to-one -> utilisateur  v
    utilisateurCompetent = models.ForeignKey(Utilisateur, related_name="CourCompetenceUser-cours")
    competence = models.OneToOneField(CourCompetence, related_name="CompetenceInCourCompetenceUser")
    def __unicode__(self):
        return self.CourCompetence.__unicode__() + " : " + self.utilisateurCompetent.__unicode__()
