from django.urls import path
from . import views
urlpatterns=[
    path("leads_list/",views.Leads_list,name="leads_list")
]