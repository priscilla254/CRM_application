from django.urls import path
from . import views
urlpatterns=[
    path('note/',views.take_notes,name="note")

]


