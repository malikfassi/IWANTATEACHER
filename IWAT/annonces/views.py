from django.shortcuts import render
from datetime import datetime
from annonces.models import Annonce

def getLastAnnouncement(request):
	lastAnnouncement = Annonce.objects.order_by('posterLe')[:5]
	context = {"lastAnnouncement":lastAnnouncement}
	return render(request, 'display.html', context)

from django.shortcuts import render_to_response
from cours.forms import ContexteForm, CourCompetenceForm
from cours.models import CourEvenement, CourCompetence
from django.template import RequestContext
from login.views import getLoggedUserFromRequest
from login.models import Utilisateur

def postAnnonce(request):
	if "loggedUserId" in request.session:
		if request.GET:
			formulaireContexte = ContexteForm(request.GET)
			formulaireMatiere = CourCompetenceForm(request.GET)
			formulaireContexte.secteur = "FR"
			formulaireMatiere.anneeSecteur = "S3"
			message = 'Il y a des erreurs dans le formulaire'
			if(formulaireMatiere.is_valid() and formulaireContexte.is_valid()):
				message = 'Annonce postee!'
				contexte = CourEvenement(sujet=getMatiere(), heure=formulaireContexte.cleared_data['heure'], lieu=formulaireContexte.cleared_data['lieu'], eleve=request.session['loggedUserId'], prof=formulaireContexte['prof'])
				newContexte = contexte.save()
				newAnnonce = Annonce(contexte=newContexte, posterPar=userId, posterLe=timezone.now())
				newAnnonce.save()
				return render_to_response("postAnnonce.html", RequestContext(request, {'contexteForm':'', 'competenceForm':'', 'message':message}))
			return render_to_response("postAnnonce.html", RequestContext(request, {'contexteForm':formulaireContexte, 'competenceForm':formulaireMatiere, 'message':message}))
		else:
				formulaireContexte = ContexteForm()
				formulaireMatiere = CourCompetenceForm()
				message = ''
				return render_to_response("postAnnonce.html", RequestContext(request, {'contexteForm':formulaireContexte, 'competenceForm':formulaireMatiere, 'message':message}))
	else:
		formulaireContexte = ""
		formulaireMatiere = ""
		message="Connectez-vous pour acceder a cette page"
	return render_to_response("postAnnonce.html", RequestContext(request, {'contexteForm':formulaireContexte, 'competenceForm':formulaireMatiere, 'message':message}))

def getMatiere(pSecteur, pAnneeSecteur):
	alreadyExist = CourCompetence.objects.all()
	for i in alreadyExist:
		if(i.secteur == pSecteur and i.anneeSecteur == pAnneeSecteur):
			return i

	nvlMatiere = CourCompetence(secteur=pSecteur, anneeSecteur=pAnneeSecteur)
	return nvlMatiere.save()
