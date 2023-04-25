import sys
sys.path.append("../../")

from django.shortcuts import render
from scheduler.models import Event
from django.http import HttpResponseRedirect
from datetime import datetime
from apis.accu_getter import ACCU_getter



def todo_list(request):
    events = Event.objects.filter(is_complete=False)
    from datetime import datetime, timedelta
    for event in events:
        try:
            now = datetime.now()
            change = timedelta(hours=10)
            date = now + change
            place = event.event_city
            getter = ACCU_getter()
            event.has_high_pollen = getter.get_warnings(date, place)
        except:
            pass
    return render(request, "todo_list.html", {"events": events})

def completed_task(request):
    event_name = request.POST.get('markcomplete')
    Event.objects.filter(event_name=event_name).update(is_complete=True)
    #Event.objects.filter(event_name=event_name).delete()
    return HttpResponseRedirect('/todo_list/')

def new_task(request):
    #print(request.POST)
    name = request.POST.get('event_name')
    start_str = request.POST.get('start_time')
    start = datetime.now()
    if start_str != "":
        start = datetime.strptime(start_str, '%Y-%m-%dT%H:%M')
    
    end_str = request.POST.get('end_time')
    end = datetime.now()
    if end_str != "":
        end = datetime.strptime(end_str, '%Y-%m-%dT%H:%M')
    
    address = request.POST.get('address')
    city = request.POST.get('city')
    
    zip_str = request.POST.get('zip_code')
    zip = 0
    if zip_str != "":
        zip = int(zip_str)
    
    outside_str = request.POST.get('in_out')
    outside = False
    if outside_str != "":
        outside = bool(outside_str)
    event = Event.objects.create(event_name=name, start_time=start, end_time=end, event_street_address=address, event_city=city, event_zipcode=zip, is_outdoors=outside)
    return HttpResponseRedirect('/todo_list/')