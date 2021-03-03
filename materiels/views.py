from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='acces')

# Create your views here.
def dashbord(request):
    
        
    datas={
        
    }
    
    return render(request,'base/index.html',datas)
