
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from login.models import LoginForm
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
    c = RequestContext(request,{'message':state, 'form':form})
    return render_to_response('login.html',c)

def main_page(request):
    return render_to_response('index.html')
 
def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')