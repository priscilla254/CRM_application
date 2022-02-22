from django.shortcuts import render
from .models import Lead

def Leads_list(request):
    leads=Lead.objects.all()
    context={'leads':leads}
    return render(request,"leads/leads_list.html",context)
