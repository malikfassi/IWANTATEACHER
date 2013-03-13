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

def postAnnonce(request):
	if request.GET and 'loggedUserId' in request.session:
		formulaireContexte = ContexteForm(request.GET)
		formulaireMatiere = CourCompetenceForm(request.GET)
		if(formulaireMatiere.is_valid() and formulaireContexte.is_valid()):
			contexte = CourEvenement(sujet=getMatiere(), heure=formulaireContexte.cleared_data['heure'], lieu=formulaireContexte.cleared_data['lieu'], eleve=request.session['loggedUserId'], prof=formulaireContexte['prof'])
			newContexte = contexte.save()
			newAnnonce = Annonce(contexte=newContexte, posterPar=request.session['loggedUserId'], posterLe=timezone.now())
			newAnnonce.save()
			return render_to_response("postAnnonce.html", RequestContext(request, {'contexteForm':formulaireContexte, 'competenceForm':formulaireMatiere, 'message':"Annonce postee vaec succes!"}))
		else:
			return render_to_response("postAnnonce.html", RequestContext(request, {'contexteForm':formulaireContexte, 'competenceForm':formulaireMatiere, 'message':"Il ya des champs erones dans le formulaire"}))
	else:
		formulaireContexte = ContexteForm()
		formulaireMatiere = CourCompetenceForm()
	return render_to_response("postAnnonce.html", RequestContext(request, {'contexteForm':formulaireContexte, 'competenceForm':formulaireMatiere, 'message':"Il faut etre identifier pour poster"}))

def getMatiere(pSecteur, pAnneeSecteur):
	alreadyExist = CourCompetence.objects.all()
	for i in alreadyExist:
		if(i.secteur == pSecteur and i.anneeSecteur == pAnneeSecteur):
			return i

	nvlMatiere = CourCompetence(secteur=pSecteur, anneeSecteur=pAnneeSecteur)
	return nvlMatiere.save()
