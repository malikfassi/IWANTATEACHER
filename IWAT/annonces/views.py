from django.shortcuts import render

from annonces.models import Annonce

def getLastAnnouncement(request):
	lastAnnouncement = Annonce.objects.order_by('posterLe')[:5]
	context = {"lastAnnouncement":lastAnnouncement}
	return render(request, 'display.html', context)