from django.shortcuts import render
from .models import *

def Leads_list(request):
    leads=Lead.objects.all()
    context={'leads':leads}
    return render(request,"leads/leads_list.html",context)

def Contacts_list(request):
    contacts=Contact.objects.all()
    context={'contacts':contacts}
    return render(request,"leads/contacts_list.html",context)

def Opportunity_list(request):
    opportunities=Opportunity.objects.all()
    context={'opportunities':opportunities}
    return render(request,'leads/opportunities_list.html',context)