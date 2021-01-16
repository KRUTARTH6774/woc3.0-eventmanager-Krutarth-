from django.contrib import admin
from django.urls import path
from event import views

urlpatterns = [
    path("",views.base,name='base'),
    path("event_registration",views.event_registration,name='event_registration'),
    path("event_dashboard",views.event_dashboard,name='event_dashboard'),
    path("participant_registration",views.participant_registration,name='participant_registration')
]