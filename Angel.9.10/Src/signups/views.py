from django.shortcuts import render, render_to_response, redirect ,RequestContext
from .forms import SignUpForm
# Create your views here.
from .models import SignUp

def registration(request):  
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit = False)
        save_it.save()
    return render_to_response("signup.html",locals(),context_instance = RequestContext(request))
def login(request):
    context = {}
    template="login.html"
    return render(request,template,context)