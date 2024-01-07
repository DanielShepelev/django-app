from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from business_logic.forms import UserPrefrencesForm
from authentication.models import FoodiUser

def redirect_to_authentication(request,destnation):
    # Specify the URL pattern of the target view within the other app
    authentication_url = f'/auth/{destnation}/' 

    # Use the redirect function to perform the redirection
    return redirect(authentication_url)


# Create your views here.
@login_required(login_url='/auth/login/')
def home_view(request):
    if request.user.prefrence == {}:
        return redirect('welcome')
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect_to_authentication(request,'login')

@login_required(login_url='/auth/login/')
def welcome_view(request):
    if request.method == 'POST':
        prefrenceForm = UserPrefrencesForm(request.POST)
        if prefrenceForm.is_valid():
            dictFoodi = createDict(prefrenceForm)
            user_instance = request.user
            user_instance.prefrence = dictFoodi
            user_instance.save() 
            return redirect('home')
    return render(request, 'welcome.html')

def createDict(form):
    dictFoodi = {}
    dictFoodi["foodPrefrence"] = list(form.cleaned_data['foodPrefrence'])
    dictFoodi["restricstions"] = form.cleaned_data['restricstions']
    dictFoodi["city"] = form.cleaned_data['city']
    return dictFoodi
