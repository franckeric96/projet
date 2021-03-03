from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreerUtilisateur
from django.contrib import messages

# Create your views here.
def inscriptionPage(request):
    
    form=CreerUtilisateur()
    if request.method=='POST':
        form=CreerUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            return redirect('acces')
        
    datas={'form':form,
        
    }
    
    return render(request,'utilisateurs/inscription.html',datas)

def accesPage(request):
    message=""
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('dashbord')
        else:
            message="oups les informations sont incorrectes!"

    datas={
    'message':message,
}
    return render(request,'utilisateurs/acces.html',datas)


def logoutUser(request):
    
    logout(request)
    
    return redirect('acces')