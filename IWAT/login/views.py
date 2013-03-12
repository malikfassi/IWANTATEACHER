
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from login.forms import LoginForm, SignInForm, UtilisateurForm
from login.models import Utilisateur
from django.template import RequestContext

def login_user(request):
    state = "Please log in below..."
    if request.POST:
        form = LoginForm(request.POST)
        if(form.is_valid()):
            user = authenticate(username = form.cleaned_data['pseudo'], password=form.cleaned_data['mdp'])
            if user is not None:
                state = 'logged in'
    else:
        form = LoginForm()
    context = RequestContext(request,{'message':state, 'form':form})
    return render_to_response('login.html',context)

def main_page(request):
    return render_to_response('index.html')
 
def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')

def signin(request):
    if request.GET:
        formUser = SignInForm(request.GET)
        formUtilisateur = UtilisateurForm(request.GET)
        if formUser.is_valid() and formUtilisateur.is_valid():
            user=formUser.save()
            user.set_password(formUser.cleaned_data["password"])
            user.save()
            utilisateur = Utilisateur(profilBase=user, birthday=formUtilisateur.cleaned_data["birthday"])
            utilisateur.save()
            return(HttpResponseRedirect('/login'))
        else:
            return(render_to_response("signin.html",{"formUser":formUser, "formUtilisateur":formUtilisateur}))
    else:
        formUser = SignInForm()
        formUtilisateur = UtilisateurForm()
        context = RequestContext(request,{"formUser":formUser, "formUtilisateur":formUtilisateur})
        return(render_to_response("signin.html",context))
