# authentication/views.py
from django.shortcuts import render, redirect
from django import forms
from .forms import UserForm,UserAuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def redirect_to_business_logic(request,destnation):
    # Specify the URL pattern of the target view within the other app
    business_logic_url = f'/services/{destnation}/' 

    # Use the redirect function to perform the redirection
    return redirect(business_logic_url)


def login_view(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                if user.prefrence == {}:
                    return redirect_to_business_logic(request,'welcome')
                return redirect_to_business_logic(request,'home')  # Redirect to the home page or any desired page after successful login
            else:
                # Invalid credentials
                return render(request, 'login.html')
    
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            save_form=form.save(commit=False)
            save_form.set_password(form.cleaned_data['password'])
            save_form.prefrence = request.POST.get('prefrence', {})
            save_form.status = 1
            save_form.save()
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect_to_business_logic(request,'welcome')
            else:
                # Invalid credentials
                return render(request, 'login.html')
            
    return render(request, 'signup.html')



