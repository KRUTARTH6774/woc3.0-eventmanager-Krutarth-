from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,'base.html')
def event_registration(request):
    return render(request,'event_registration.html')
def event_dashboard(request):
    return render(request,'event_dashboard.html')
def participant_registration(request):
    return render(request,'participant_registration.html')
