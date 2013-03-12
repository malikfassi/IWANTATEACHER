from django.shortcuts import render

from annonces.models import Annonce

def getLastAnnouncement(request):
	lastAnnouncement = Annonce.objects.order_by('posterLe')[:5]
	context = {"lastAnnouncement":lastAnnouncement}
	return render(request, 'display.html', context)

from annonces.models import AnnonceForm
from django.shortcuts import render_to_response

def postAnnonce(request):
	
	return render_to_response("postAnnonce.html",{"form":AnnonceForm()})
