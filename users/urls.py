
from django.urls import path
from . import views
 

urlpatterns=[
    path('',views.Home,name="dashboard"),
     path('register/',views.RegisterView,name="register"),
    path('login/',views.LoginView,name="login"),
    path('logout/',views.LogoutView,name="logout"),
    path('contact_us/',views.ContactView,name="contact_us"),
]