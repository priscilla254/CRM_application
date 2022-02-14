from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout   


def Home(request):
    return render(request,'users/dashboard.html')

