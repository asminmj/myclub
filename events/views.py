from django.shortcuts import render, redirect
import calendar 
from calendar import HTMLCalendar
from datetime import datetime 
from .models import Event, Venue 
from .forms import VenueForm, EventForm 
from django.http import HttpResponseRedirect

#delete an event
def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list-venues')

#delete an event
def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('list-events')



# Create your views here.
def add_event(request):
    submitted = False 
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm 
        if 'submitted' in request.GET:
            submitted = True 
    form = EventForm
    return render(request, 'add_event.html', {'form':form,'submitted':submitted,})

def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event,)
    if form.is_valid():
        form.save()
        return redirect('list-events')

    return render(request, 'update_event.html', {'event':event, 'form':form,})

def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue,)
    if form.is_valid():
        form.save()
        return redirect('list-venues')

    return render(request, 'update_venue.html', {'venue':venue, 'form':form,})



def search_venues(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched,)
        return render(request, 'search_venues.html', {'searched':searched, 'venues':venues,})
    else:
        return render(request, 'search_venues.html', {})
   


def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'show_venue.html', {'venue':venue,})

    
def list_venues(request):
    venue_list = Venue.objects.all()
    return render(request, 'venue.html', {'venue_list': venue_list,})


def add_venue(request):
    submitted = False 
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm 
        if 'submitted' in request.GET:
            submitted = True 
    form = VenueForm
    return render(request, 'add_venue.html', {'form':form,'submitted':submitted,})

def all_events(request):
    event_list = Event.objects.all().order_by('name', 'venue')
    return render(request, 'event_list.html', {'event_list':event_list})




def home(request, year=datetime.now().year, month=datetime.now().strftime('%B'),):
    #convet month from name to number 
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)


    #create a calendar 
    cal = HTMLCalendar().formatmonth(year, month_number)
    # get current year 
    now = datetime.now()
    current_year = now.year
    #GET CURRENT TIME 
    time = now.strftime('%I:%M:%S %p')
    return render(request, 
    ('home.html'), {
        "year":year,
        "month":month,
        "month_number": month_number,
        "cal":cal,
        "current_year":current_year,
        "time":time,
    })
    
