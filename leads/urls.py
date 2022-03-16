from django.urls import path
from . import views
urlpatterns=[
    path("leads_list/",views.Leads_list,name="leads_list"),
    path("opportunities_list/",views.Opportunity_list,name="opportunities_list"),
    path("contacts_list/",views.Contacts_list,name="contacts_list")
]