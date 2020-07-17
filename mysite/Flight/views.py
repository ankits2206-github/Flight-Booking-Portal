from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from . models import Flight,Passenger,Airport,Bookings
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "flights": Flight.objects.all(),
        "airports": Airport.objects.all()
    }
    return render(request,'Flight/index.html',context)



def airport(request):
    context={
        "airports": Airport.objects.all()
    }
    return render(request,'Flight/airport.html',context)


def passenger(request):
    context={
        "passengers":Passenger.objects.all()
    }
    return render(request,'Flight/passenger.html',context)

def mybookings(request):
    context={
        "mybookings":Bookings.objects.filter(date__gte = date.today())
    }

    return render(request,'Flight/mybookings.html',context)

def History(request):
    p=Bookings.objects.filter(date__lt = date.today())
    context = {
        "History": p
    }
    return render(request,'Flight/History.html',context)


def flight(request,flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)

    except Flight.DoesNotExist:
        raise Http404("Flight Does not exist.")

    context={
        "flight" : flight,
        "passengers": flight.passengers.all(),
        "non_passengers":Passenger.objects.exclude(flights=flight).all()
    }
    return render(request,'Flight/flight.html',context)



def book(request,flight_id):
    try:
        passenger_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk=passenger_id)
        flight = Flight.objects.get(pk=flight_id)

    except KeyError:
        return render(request,"Flight/error.html",{"message":"No selection."})
    except Flight.DoesNotExist:
        return render(request,"Flight/error.html",{"message":"No Flight"})
    except Passenger.DoesNotExist:
        return render(request,"Flight/error.html",{"message":"No passenger"})

    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse("flight",args=(flight_id,)))


def bookairport(request):
    try:
        city_name = request.POST["city"]
        cd = request.POST["code"]

    except KeyError:
        messages.info(request, 'Fill the full form')
        return HttpResponseRedirect(reverse("airport"))

    f=Airport(code=cd,city=city_name)
    f.save()
    return HttpResponseRedirect(reverse("airport"))


def bookpassenger(request):
    try:
        first_name = request.POST["first"]
        last_name = request.POST["last"]
        age = request.POST["age"]

    except KeyError:
        messages.info(request, 'Fill the full form')
        return HttpResponseRedirect(reverse("passenger"))

    f=Passenger(first=first_name,last=last_name,age = age)
    f.save()
    return HttpResponseRedirect(reverse("passenger"))


def addflight(request):
    try:
        f1 = request.POST["origin"]
        f2 = request.POST["destination"]
        dr = request.POST["duration"]
        d1 = Airport.objects.get(city=f1)
        d2 = Airport.objects.get(city=f2)
        print(f1,f2)


    except KeyError:
        messages.info(request, 'Please select the flight')
        return HttpResponseRedirect(reverse("index"))

    except Airport.DoesNotExist:
        messages.info(request, 'Flight Does not Exist')
        return HttpResponseRedirect(reverse("index"))


    if(f1==f2):
        messages.info(request, 'Origin and destination can not be same')
        return HttpResponseRedirect(reverse("index"))

    s1=Flight.objects.filter(origin=d1,destination=d2).exists()

    if(s1==True):
        messages.info(request, 'Flight Already exists')
        return HttpResponseRedirect(reverse("index"))

    s=Flight(origin=d1,destination=d2,duration=dr)
    s.save()
    return HttpResponseRedirect(reverse("index"))


def normregister(request,flight_id):
    try:
        first_name = request.POST['first']
        last_name= request.POST['second']
        dt = request.POST['date']
        age = request.POST['age']

    except KeyError:
        messages.info(request, 'Fill the full form')
        return HttpResponseRedirect(reverse("flight", args=(flight_id,)))

    d=date.today()
    s=date(int(dt[:4]), int(dt[5:7]), int(dt[8:10]))

    if(s<d):
        messages.info(request, 'Invalid Date')
        return HttpResponseRedirect(reverse("flight", args=(flight_id,)))


    f = Passenger(first=first_name,last=last_name,age=age)
    f.save()

    fl=Flight.objects.get(pk=flight_id)
    f.flights.add(fl)

    b=Bookings(bookedby = request.user,bookedfor = f,route = fl,date=dt)
    b.save()
    return HttpResponseRedirect(reverse("flight", args=(flight_id,)))



def delete(request):
    try:
        f=request.POST['passenger']

    except KeyError:
        messages.info(request, 'Invalid Date')
        return HttpResponseRedirect(reverse("mybookings"))

    f1=Bookings.objects.get(pk=f)
    f2 = Bookings.objects.filter(pk=f)
    p=Passenger.objects.get(pk = f1.bookedfor.id)

    p.delete()
    f2.delete()
    return HttpResponseRedirect(reverse("mybookings"))





















