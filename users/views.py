from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout   
from django.contrib import messages
from .forms import *
from django.core.mail import send_mail
def Home(request):
    return render(request,'users/dashboard.html')

def RegisterView(request):
    form =CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            

            UserProfile.objects.create(
                user=user
            )

            messages.success(request,'account was created for '+username)
            return redirect('login')
    context={'form':form}
    return render(request,'users/register.html',context)

def LoginView(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Username OR password")
    context={}
    return render(request,'users/login.html',context)
def LogoutView(request):
    logout(request)
    messages.info(request,"you have successfully logged out.")
    return redirect('/')

def ContactView(request):
    if request.method=='POST':
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()
        send_mail(
            name, # subject
            subject, #message
            email,#from email
            ['baiyawambui8@gmail.com'],
        )
        return render(request,'users/contact_us.html',{'name':name})
    return render(request,'users/contact_us.html')
