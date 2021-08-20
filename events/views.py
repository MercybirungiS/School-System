from django import forms
from django.shortcuts import render
from .forms import EventsForm
from .models import Events
from events.models import Events


# Create your views here.
def register_event (request):
    if request.method=="POST":
       form=EventsForm(request.POST , request.FILES)
       if form.is_valid():
            form.save()
       else:
            print(form.errors)
    else:
        form=EventsForm()
    return render(request,"register_event.html",{"form":form})

def events_list(request):
    events=Events.objects.all()
    return render(request,"event_list.html",{"events" :events})

