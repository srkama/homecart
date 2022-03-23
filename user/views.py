from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm


# Create your views here.
def signup(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            username = signup_form.cleaned_data['username']
            password = signup_form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        signup_form = SignupForm()
    return render(request, 'signup.html', {'form': signup_form})