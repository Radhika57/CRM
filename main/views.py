from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q
from Useraccount.models import User
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import TemplateView,UpdateView
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .serializers import LeadModelSerializer, CustomerModelSerializer, SupplierModelSerializer, SightseeingModelSerializer
from .serializers import HotelModelSerializer, PackageModelSerializer, UserModelSerializer, VehicleModelSerializer
from rest_framework import status
from django.contrib.auth.decorators import login_required
from .forms import *
from Useraccount.forms import UserForm
from django.shortcuts import render
from django.views import generic
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from random import random
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import UpdateView , CreateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
import uuid



#################################### Front Display  #########################################

def maincontent(Request):
    return render(Request, "maincontent.html")

def about(Request):
    return render(Request, "about.html")


def features(Request):
    return render(Request, "travocrm.html")


def calendy(Request):
    return render(Request, "calendy.html")


def clients(Request):
    return render(Request, "clients.html")


def contactus(Request):
    return render(Request, "contactus.html")


def pricing(Request):
    return render(Request, "pricing.html")


def privacypolicy(Request):
    return render(Request, "privacypolicy.html")


def termsandconditions(Request):
    return render(Request, "termsandconditions.html")

#################################### End Front Display ###################################



#################################### Dashboard Start ###################################

def dashboard(Request):
    d2 = Lead.objects.filter(priority="Hot")
    d3 = Lead.objects.filter(priority="Hot").count()
    d4 = Lead.objects.all().count()
    d5 = Lead.objects.filter(status="Booked").count()
    d6 = Lead.objects.filter(status="Lost").count()
    whatsappnumber =WhatsAppNumber.objects.all().last()
    return render(Request, "dashboard.html",{'d2':d2,'d3':d3,'d4':d4,'d5':d5,'d6':d6,'whatsappnumber':whatsappnumber})

def logoutPage(Request):
    logout(Request)
    return redirect("/login")

def viewProfile(Request,id):
    d = User.objects.get(id=id)
    return render(Request, "viewprofile.html", {"d": d})


#################################### End Dashboard ###################################

#################################### Start Lead  ###################################

def leads(Request):
    type = Request.user.type
    if type == "Admin":
        data = Lead.objects.all()
        d1 = User.objects.all()
        if Request.method == 'POST':
        # from_date = Request.POST.get('from')
        # to_date = Request.POST.get('to')
            priority = Request.POST.get('priority')
            status = Request.POST.get('status')
            triptype = Request.POST.get('triptype')
            assigned = Request.POST.get('assigned')
            # enquiry_type = Request.POST.get('enquiry')
            leadno = Request.POST.get('leadnumber')
            firstname = Request.POST.get('firstname')
            lastname = Request.POST.get('lastname')
            number = Request.POST.get('mobilenumber')
            email = Request.POST.get('email')
            tags = Request.POST.get('tags')
            data = Lead.objects.filter(Q(priority=priority)|Q(status=status)|Q(triptype=triptype)|Q(assigned=assigned)|Q(leadno=leadno)
                               |Q(firstname=firstname)|Q(lastname=lastname)|Q(number=number)|Q(email=email)|Q(tags=tags))
            return render(Request, "leads.html", {'d1':d1,'data':data})
        return render(Request, "leads.html", {'d1':d1,'data':data})
    else:
        #data = Lead.objects.all()
        data = Lead.objects.filter(assigned=Request.user)
        d1 = User.objects.get(email = Request.user.email)
        if Request.method == 'POST':
        # from_date = Request.POST.get('from')
        # to_date = Request.POST.get('to')
            priority = Request.POST.get('priority')
            status = Request.POST.get('status')
            triptype = Request.POST.get('triptype')
            assigned = Request.POST.get('assigned')
            # enquiry_type = Request.POST.get('enquiry')
            leadno = Request.POST.get('leadnumber')
            firstname = Request.POST.get('firstname')
            lastname = Request.POST.get('lastname')
            number = Request.POST.get('mobilenumber')
            email = Request.POST.get('email')
            tags = Request.POST.get('tags')
            print(Request.POST)
            data = Lead.objects.filter(Q(priority=priority)|Q(status=status)|Q(triptype=triptype)|Q(assigned=assigned)|Q(leadno=leadno)
                               |Q(firstname=firstname)|Q(lastname=lastname)|Q(number=number)|Q(email=email)|Q(tags=tags))
            return render(Request, "leads.html", {'d1':d1,'data':data})
        return render(Request, "leads.html", {'d1':d1,'data':data})
from django.db import transaction

# def addleads(Request):
#         d1 = User.objects.get(email = Request.user.email)
#         if (Request.method == "POST"):
#             customertype = Request.POST.get('customertype')
#             number = Request.POST.get('number')
#             email = Request.POST.get('email')
#             salutation = Request.POST.get('salutation')
#             firstname = Request.POST.get('firstname')
#             lastname = Request.POST.get('lastname')
#             address = Request.POST.get('address')
#             city = Request.POST.get('city')
#             alternatenumber = Request.POST.get('alternatenumber')
#             alternateemail = Request.POST.get('alternateemail')
#             leadsource = Request.POST.get('leadsource')
#             priority = Request.POST.get('priority')
#             status = Request.POST.get('status')
#             adults = Request.POST.get('adults')
#             child = Request.POST.get('child')
#             infants = Request.POST.get('infants')
#             tags = Request.POST.get('tags')
#             triptype = Request.POST.get('triptype')
#             assigned = Request.POST.get('assigned')
#             created = Request.POST.get('setdate')
#             flight_booking = bool(Request.POST.get('flight_booking', False))
#             hotel_booking = bool(Request.POST.get('hotel_booking', False))
#             visa = bool(Request.POST.get('visa', False))
#             travel_insurance = bool(Request.POST.get('travel_insurance', False))
#             forex = bool(Request.POST.get('forex', False))
#             sightseeing = bool(Request.POST.get('sightseeing', False))
#             transport = bool(Request.POST.get('transport', False))
#             other = bool(Request.POST.get('other', False))
#             package = bool(Request.POST.get('package', False))
#             customized_package =bool (Request.POST.get('customized_package', False))
#             bus = bool(Request.POST.get('bus', False))
#             train = bool(Request.POST.get('train', False))
#             passport = bool(Request.POST.get('passport', False))
#             cruise = bool(Request.POST.get('cruise', False))
#             adventure = bool(Request.POST.get('adventure', False))
#             group = bool(Request.POST.get('group', False))
#             # for flite
            
#             dep_from = Request.POST.getlist('flight_from')
            
#             dep_to = Request.POST.getlist('flight_to')
#             departure = Request.POST.getlist('flight_departure')
#             return_to = Request.POST.getlist('flight_return')
#             classes = Request.POST.getlist('flight_class')
#             domestic_flight = bool(Request.POST.getlist('category_domestic_flight'))
#             internation_flight = bool(Request.POST.getlist('category_international_flight'))
#             flexibility = Request.POST.getlist('flight_flexibity')
#             preference = Request.POST.getlist('flight_preference')
            
#             #for hotel
#             hcountry = Request.POST.getlist('country')
#             hcity = Request.POST.getlist('city')
#             roomtype = Request.POST.getlist('room')
#             rating = Request.POST.getlist('rating')
#             checkin = Request.POST.getlist('checkin')
#             checkout = Request.POST.getlist('checkout')
#             nights = Request.POST.getlist('night')
#             budget = Request.POST.getlist('budget')
#             Hotelname = Request.POST.getlist('hotelname')
#             rooms = Request.POST.getlist('rooms')
            
#             #for visa
#             country = Request.POST.getlist('country')
#             visa_category = Request.POST.getlist('visa_category')
#             visit_type = Request.POST.getlist('visit_type')
#             duration = Request.POST.getlist('duration')
#             traveldate = Request.POST.getlist('traveldate')
#             job_profile = Request.POST.getlist('job_profile')
#             age = Request.POST.getlist('age')
#             qualification = Request.POST.getlist('qualification')
#             description = Request.POST.getlist('description')
            
#             #for travel_insurance
#             country = Request.POST.getlist('country')
#             how_long = Request.POST.getlist('how_long')
#             travel_date = Request.POST.getlist('travel_date')
#             insurace = Request.POST.getlist('insurace')
            
#             #for forex
#             currency = Request.POST.getlist('currency')
#             amount = Request.POST.getlist('amount')
            
#             #for sightseen
#             country = Request.POST.getlist('country')
#             city = Request.POST.getlist('city')
#             sightseen_options = Request.POST.getlist('sightseen_options')
#             preference = Request.POST.getlist('preference')
#             travel_date = Request.POST.getlist('travel_date')
            
#             #for transport
#             country = Request.POST.getlist('country')
#             city = Request.POST.getlist('city')
#             trasport_date = Request.POST.getlist('trasport_date')
#             drop_date = Request.POST.getlist('drop_date')
#             preference = Request.POST.getlist('preference')
#             Airport_transfers = bool(Request.POST.get('Airport_transfers'))
#             Sightseeing_transfers = bool(Request.POST.get('Sightseeing_transfers'))
#             Others = bool(Request.POST.get('Others'))
            
#             #for other
#             country = Request.POST.getlist('country')
#             travel_date = Request.POST.getlist('travel_date')
#             no_of_days = Request.POST.getlist('no_of_days')
#             sub_category = Request.POST.getlist('sub_category')
#             description = Request.POST.getlist('description')
            
#             #for package
#             country = Request.POST.getlist('country')
#             travel_date = Request.POST.getlist('travel_date')
#             budget = Request.POST.getlist('budget')
#             package_name  = Request.POST.getlist('package_name ')
#             extra_details  = Request.POST.getlist('extra_details ')
            
#             #for customized_package
#             country = Request.POST.getlist('country')
#             service = Request.POST.getlist('service')
#             rating = Request.POST.getlist('rating')
#             travel_date  = Request.POST.getlist('travel_date')
#             no_of_night  = Request.POST.getlist('no_of_night')
#             preferance  = Request.POST.getlist('preferance')
#             flexibility = Request.POST.getlist('flexibility')
#             no_of_rooms = Request.POST.getlist('no_of_rooms')
#             rating = Request.POST.getlist('rating')
#             budget  = Request.POST.getlist('budget')
#             description  = Request.POST.getlist('description')
            
#             #for bus
#             country = Request.POST.getlist('country')
#             From = Request.POST.getlist('From')
#             to = Request.POST.getlist('to')
#             departure  = Request.POST.getlist('departure ')
#             Return  = Request.POST.getlist('Return ')
#             preference  = Request.POST.getlist('preference ')
#             remark   = Request.POST.getlist('remark ')
            
#             #for train
#             country = Request.POST.getlist('country')
#             From = Request.POST.getlist('From')
#             to = Request.POST.getlist('to')
#             departure  = Request.POST.getlist('departure ')
#             Return  = Request.POST.getlist('Return ')
#             preference  = Request.POST.getlist('preference')
#             remark  = Request.POST.getlist('remark ')
            
#             #for passport
#             country = Request.POST.getlist('country')
#             date = Request.POST.getlist('date')
#             passport_no = Request.POST.getlist('passport_no')
#             place_of_apply  = Request.POST.getlist('place_of_apply ')
#             no_of_person  = Request.POST.getlist('no_of_person')
#             new_passport = bool(Request.POST.get('new_passport'))
#             renew_passport = bool(Request.POST.get('renew_passport'))
#             urgent = bool(Request.POST.get('urgent'))
#             remark  = Request.POST.getlist('remark ')
            
#             #for cruise
#             country = Request.POST.getlist('country')
#             City = Request.POST.getlist('City')
#             days = Request.POST.getlist('days')
#             Cruise_name  = Request.POST.getlist('Cruise_name ')
#             type  = Request.POST.getlist('type ')
#             departure = Request.POST.getlist('departure')
#             Return = Request.POST.getlist('Return')
#             room_type  = Request.POST.getlist('room_type ')
#             remark  = Request.POST.getlist('remark ')
            
#             #for adventure
#             country = Request.POST.getlist('country')
#             city = Request.POST.getlist('city')
#             travel_date = Request.POST.getlist('travel_date')
#             motorbiking = bool(Request.POST.get('motorbiking'))
#             camping = bool(Request.POST.get('camping'))
#             safari = bool(Request.POST.get('safari'))
#             water_sports = bool(Request.POST.get('water_sports'))
#             remark  = Request.POST.getlist('remark ')
           
#             #for group
#             country = Request.POST.getlist('country')
#             package_name = Request.POST.getlist('package_name')
#             preference = Request.POST.getlist('preference')
#             remark  = Request.POST.getlist('remark ')
                     
#             data = Lead.objects.create(customertype=customertype, number=number, email=email, salutation=salutation, firstname=firstname, lastname=lastname, address=address,
#                         city=city, alternatenumber=alternatenumber, alternateemail=alternateemail, leadsource=leadsource, priority=priority, status=status,
#                         adults=adults, child=child, infants=infants, tags=tags,triptype=triptype, assigned=Request.user, created=created,flight_booking=flight_booking, hotel_booking=hotel_booking, visa=visa,
#                        travel_insurance=travel_insurance,forex=forex,sightseeing=sightseeing,transport=transport,other=other,package=package,customized_package=customized_package,bus=bus,
#                        train=train,passport=passport,cruise=cruise,adventure=adventure,group=group
#                     )
#             print(data.leadno)
#             print(data)
#             if data.flight_booking:
#                 print(dep_from,dep_to)

#                 for i in dep_from:
                    
#                     data1 = Flight_booking(leads=data,dep_from=i,dep_to=dep_to,departure=departure,return_to=return_to,
#                                     classes=classes,domestic_flight=domestic_flight,internation_flight=internation_flight,
#                                     flexibility=flexibility,preference=preference)
#                     print(i)
#                     data1.save()
                    
#                 #     data1 = Flight_booking(leads=data.leadno,dep_from=dep_from[i],dep_to=dep_to[i],departure=departure[i],return_to=return_to[i],
#                 #                     classes=classes[i],domestic_flight=domestic_flight,internation_flight=internation_flight,
#                 #                     flexibility=flexibility[i],preference=preference[i])
#                 #     data1.save()
                    
#             if data.hotel_booking:
#                 data2 = Hotel_booking(leads=data,hcountry=hcountry,hcity=hcity,roomtype=roomtype,rating=rating,checkin=checkin,
#                                     checkout=checkout, nights=nights,budget=budget,Hotelname=Hotelname,rooms=rooms)
#                 data2.save()
                
#             if data.visa:
#                 data3 = Visa_booking(leads=data,country=country,visa_category=visa_category,visit_type=visit_type,duration=duration,traveldate=traveldate,
#                                     job_profile=job_profile, age=age,qualification=qualification,description=description)
#                 data3.save()
                
#             if data.travel_insurance:
#                 data4 = Travel_insurance(leads=data,country=country,how_long=how_long,travel_date=travel_date,insurace=insurace)
#                 data4.save()
                
#             if data.forex:
#                 data5 = Forex(leads=data,currency=currency,amount=amount)
#                 data5.save()
                
#             if data.sightseeing:
#                 data6 = Sightseen(leads=data,country=country,city=city,sightseen_options=sightseen_options,preference=preference,travel_date=travel_date)
#                 data6.save()
                
#             if data.transport:
#                 data7 = Transport(leads=data,country=country,city=city,trasport_date=trasport_date,drop_date=drop_date,preference=preference,
#                                     Airport_transfers=Airport_transfers, Sightseeing_transfers=Sightseeing_transfers,Others=Others)
#                 data7.save()
                
#             if data.other:
#                 data8 = Other(leads=data,country=country,travel_date=travel_date,no_of_days=no_of_days,sub_category=sub_category,description=description)
#                 data8.save()
                
#             if data.package:
#                 data9 = Packagee(leads=data,travel_date=travel_date,budget=budget,country=country,package_name=package_name,extra_details=extra_details)
#                 data9.save()
                
#             if data.customized_package:
#                 data10 = Customized_Package(leads=data,country=country,service=service,rating=rating,travel_date=travel_date,
#                                     no_of_night=no_of_night, flexibility=flexibility,no_of_rooms=no_of_rooms,preferance=preferance,budget=budget,description=description,)
#                 data10.save()
                
#             if data.bus:
#                 data11 = Bus(leads=data,country=country,From=From,to=to,departure=departure,Return=Return,
#                                     preference=preference, remark=remark)
#                 data11.save()
                
#             if data.train:
#                 data12 = Train(leads=data,country=country,From=From,to=to,departure=departure,Return=Return,
#                                     preference=preference, remark=remark)
#                 data12.save()
                
#             if data.passport:
#                 data13 = Passport(leads=data,country=country,date=date,passport_no=passport_no,place_of_apply=place_of_apply,no_of_person=no_of_person,
#                                     new_passport=new_passport, renew_passport=renew_passport,urgent=urgent, remark=remark)
#                 data13.save()
                
#             if data.cruise:
#                 data14 = Cruise(leads=data,country=country,City=City,days=days,Cruise_name=Cruise_name,type=type,
#                                     departure=departure, Return=Return,room_type=room_type, remark=remark)
#                 data14.save()
                
#             if data.adventure:
#                 data15 = Adventure(leads=data,country=country,city=city,travel_date=travel_date,motorbiking=motorbiking,camping=camping,
#                                     safari=safari,water_sports=water_sports,remark=remark)
#                 data15.save()

#             if data.group:
#                 data16 = Group(leads=data,country=country,package_name=package_name,preference=preference,remark=remark)
#                 data16.save()
            
#         return render(Request, "addleads.html",{'d1':d1})

class LeadAddView(CreateView):
    form_class = LeadForm
    template_name = 'addlead.html'
    success_url = '/leads/'
    
    
def AddFlightBooking(request):
    form = LeadFlightForm()
    formset = FlightFormSet(queryset=Flight_booking.objects.none())

    if request.method == 'POST':
        formset = FlightFormSet(request.POST, request.FILES)
        if formset.is_valid():
            flight_instances = formset.save()
            flight_ids = [flight_instance.id for flight_instance in flight_instances]
            form = LeadFlightForm(request.POST, request.FILES)
            if form.is_valid():
                lead_instance = form.save(commit=False)
                lead_instance.user = request.user
                lead_instance.save()
                m = FlightBooking.objects.filter().last()
                m.flight.set(flight_ids)
                return redirect('/leads/')  # Redirect to the leads page
            else:
                return render(request, 'AddFlightBooking.html', {'form': form, "bird_formset": formset, 'error': form.errors})

    return render(request, 'AddFlightBooking.html', {'form': form, "bird_formset": formset})

def displayflightbooking(request):
    bookings = FlightBooking.objects.select_related('leads').prefetch_related('flight')
    return render(request, 'FlightBooking.html', {'bookings': bookings})

def AddHotelBooking(request):
    form = LeadHotelForm()
    formset = HotelFormSet(queryset=Hotel_booking.objects.none())

    if request.method == 'POST':
        formset = HotelFormSet(request.POST, request.FILES)
        if formset.is_valid():
            hotel_instances = formset.save()
            hotel_ids = [hotel_instance.id for hotel_instance in hotel_instances]
            form = LeadHotelForm(request.POST, request.FILES)
            if form.is_valid():
                lead_instance = form.save(commit=False)
                lead_instance.user = request.user
                lead_instance.save()
                m = HotelBooking.objects.filter().last()
                m.hotel.set(hotel_ids)
                return redirect('/leads/')  # Redirect to the leads page
            else:
                return render(request, 'AddHotelBooking.html', {'form': form, "bird_formset": formset, 'error': form.errors})

    return render(request, 'AddHotelBooking.html', {'form': form, "bird_formset": formset})

def displayhotelbooking(request):
    bookings = HotelBooking.objects.select_related('leads').prefetch_related('hotel')
    return render(request, 'HotelBooking.html', {'bookings': bookings})

def AddVisaBooking(request):
    form = LeadVisaForm()
    formset = VisaFormSet(queryset=Visa_booking.objects.none())

    if request.method == 'POST':
        formset = VisaFormSet(request.POST, request.FILES)
        if formset.is_valid():
            visa_instances = formset.save()
            visa_ids = [visa_instance.id for visa_instance in visa_instances]
            form = LeadVisaForm(request.POST, request.FILES)
            if form.is_valid():
                lead_instance = form.save(commit=False)
                lead_instance.user = request.user
                lead_instance.save()
                m = VisaBooking.objects.filter().last()
                m.visa.set(visa_ids)
                return redirect('/leads/')  # Redirect to the leads page
            else:
                return render(request, 'AddVisaBooking.html', {'form': form, "bird_formset": formset, 'error': form.errors})

    return render(request, 'AddVisaBooking.html', {'form': form, "bird_formset": formset})

def displayvisa(request):
    bookings = VisaBooking.objects.select_related('leads').prefetch_related('visa')
    return render(request, 'VisaBooking.html', {'bookings': bookings})

def AddTravelInsurance(request):
    form = LeadTravelForm()
    formset = TravelFormSet(queryset=Travel_insurance.objects.none())

    if request.method == 'POST':
        formset = TravelFormSet(request.POST, request.FILES)
        if formset.is_valid():
            travel_instances = formset.save()
            travel_ids = [travel_instance.id for travel_instance in travel_instances]
            form = LeadTravelForm(request.POST, request.FILES)
            if form.is_valid():
                lead_instance = form.save(commit=False)
                lead_instance.user = request.user
                lead_instance.save()
                m = TravelInsurance.objects.filter().last()
                m.travel.set(travel_ids)
                return redirect('/leads/')  # Redirect to the leads page
            else:
                return render(request, 'AddTravelInsurance.html', {'form': form, "bird_formset": formset, 'error': form.errors})

    return render(request, 'AddTravelInsurance.html', {'form': form, "bird_formset": formset})

def displaytravelinsurance(request):
    bookings = TravelInsurance.objects.select_related('leads').prefetch_related('travelinsurance')
    return render(request, 'TravelInsurance.html', {'bookings': bookings})

def AddForex(request):
    form = LeadForexForm()
    formset = ForexFormSet(queryset=Forex.objects.none())

    if request.method == 'POST':
        formset = ForexFormSet(request.POST, request.FILES)
        if formset.is_valid():
            forex_instances = formset.save()
            forex_ids = [forex_instance.id for forex_instance in forex_instances]
            form = LeadForexForm(request.POST, request.FILES)
            if form.is_valid():
                lead_instance = form.save(commit=False)
                lead_instance.user = request.user
                lead_instance.save()
                m = LeadForex.objects.filter().last()
                m.forex.set(forex_ids)
                return redirect('/leads/')  # Redirect to the leads page
            else:
                return render(request, 'AddForex.html', {'form': form, "bird_formset": formset, 'error': form.errors})

    return render(request, 'AddForex.html', {'form': form, "bird_formset": formset})

def displayforex(request):
    bookings = LeadForex.objects.select_related('leads').prefetch_related('forex')
    return render(request, 'Forex.html', {'bookings': bookings})

def AddSightseen(request):
    form = LeadSightseenForm()
    formset = SightseenFormSet(queryset=Sightseen.objects.none())

    if request.method == 'POST':
        formset = SightseenFormSet(request.POST, request.FILES)
        if formset.is_valid():
            sightseen_instances = formset.save()
            sightseen_ids = [sightseen_instance.id for sightseen_instance in sightseen_instances]
            form = LeadSightseenForm(request.POST, request.FILES)
            if form.is_valid():
                lead_instance = form.save(commit=False)
                lead_instance.user = request.user
                lead_instance.save()
                m = LeadSightseen.objects.filter().last()
                m.sightseen.set(sightseen_ids)
                return redirect('/leads/')  # Redirect to the leads page
            else:
                return render(request, 'AddSightseen.html', {'form': form, "bird_formset": formset, 'error': form.errors})

    return render(request, 'AddSightseen.html', {'form': form, "bird_formset": formset})

def displaysightseen(request):
    bookings = LeadSightseen.objects.select_related('leads').prefetch_related('sightseen')
    return render(request, 'Sightseens.html', {'bookings': bookings})

def AddTravel(request):
    form = LeadTransportForm()
    formset = TransportFormSet(queryset=Transport.objects.none())

    if request.method == 'POST':
        formset = TransportFormSet(request.POST, request.FILES)
        if formset.is_valid():
            transport_instances = formset.save()
            transport_ids = [transport_instance.id for transport_instance in transport_instances]
            form = LeadTransportForm(request.POST, request.FILES)
            if form.is_valid():
                lead_instance = form.save(commit=False)
                lead_instance.user = request.user
                lead_instance.save()
                m = LeadTransport.objects.filter().last()
                m.transport.set(transport_ids)
                return redirect('/leads/')  # Redirect to the leads page
            else:
                return render(request, 'AddTravel.html', {'form': form, "bird_formset": formset, 'error': form.errors})

    return render(request, 'AddTravel.html', {'form': form, "bird_formset": formset})

def displaytravel(request):
    bookings = LeadTransport.objects.select_related('leads').prefetch_related('transport')
    return render(request, 'TransportBooking.html', {'bookings': bookings})

def AddOther(request):
    form = LeadOtherForm()
    formset = OtherFormSet(queryset=Other.objects.none())

    if request.method == 'POST':
        formset = OtherFormSet(request.POST, request.FILES)
        if formset.is_valid():
            other_instances = formset.save()
            other_ids = [other_instance.id for other_instance in other_instances]
            form = LeadOtherForm(request.POST, request.FILES)
            if form.is_valid():
                lead_instance = form.save(commit=False)
                lead_instance.user = request.user
                lead_instance.save()
                m = LeadOther.objects.filter().last()
                m.other.set(other_ids)
                return redirect('/leads/')  # Redirect to the leads page
            else:
                return render(request, 'AddOther.html', {'form': form, "bird_formset": formset, 'error': form.errors})

    return render(request, 'AddOther.html', {'form': form, "bird_formset": formset})

def displayother(request):
    bookings = LeadOther.objects.select_related('leads').prefetch_related('other')
    return render(request, 'Other.html', {'bookings': bookings})

def AddPackagee(request):
    form = LeadPackageForm()
    formset = PackageeFormSet(queryset=Packagee.objects.none())

    if request.method == 'POST':
        formset = PackageeFormSet(request.POST, request.FILES)
        if formset.is_valid():
            package_instances = formset.save()
            package_ids = [package_instance.id for package_instance in package_instances]
            form = LeadPackageForm(request.POST, request.FILES)
            if form.is_valid():
                lead_instance = form.save(commit=False)
                lead_instance.user = request.user
                lead_instance.save()
                m = LeadPackage.objects.filter().last()
                m.package.set(package_ids)
                return redirect('/leads/')  # Redirect to the leads page
            else:
                return render(request, 'AddPackagee.html', {'form': form, "bird_formset": formset, 'error': form.errors})

    return render(request, 'AddPackagee.html', {'form': form, "bird_formset": formset})

def displaypackage(request):
    bookings = LeadPackage.objects.select_related('leads').prefetch_related('package')
    return render(request, 'PackageBooking.html', {'bookings': bookings})

def AddCustomizedPackage(request):
    form = LeadCustomizedPackageForm()
    formset = CustomizedPackageFormSet(queryset=Customized_Package.objects.none())

    if request.method == 'POST':
        formset = CustomizedPackageFormSet(request.POST, request.FILES)
        if formset.is_valid():
            customizedpackage_instances = formset.save()
            customizedpackage_ids = [customizedpackage_instance.id for customizedpackage_instance in customizedpackage_instances]
            form = LeadCustomizedPackageForm(request.POST, request.FILES)
            if form.is_valid():
                lead_instance = form.save(commit=False)
                lead_instance.user = request.user
                lead_instance.save()
                m = CustomizedPackage.objects.filter().last()
                m.customizedpackage.set(customizedpackage_ids)
                return redirect('/leads/')  # Redirect to the leads page
            else:
                return render(request, 'AddCustomizedPackage.html', {'form': form, "bird_formset": formset, 'error': form.errors})

    return render(request, 'AddCustomizedPackage.html', {'form': form, "bird_formset": formset})

def displaycustomizedpackage(request):
    bookings = CustomizedPackage.objects.select_related('leads').prefetch_related('customizedpackage')
    return render(request, 'CustomizedPacakge.html', {'bookings': bookings})

def AddBus(request):
    form = LeadBusForm()
    formset = BusFormSet(queryset=Flight_booking.objects.none())

    if request.method == 'POST':
        formset = BusFormSet(request.POST, request.FILES)
        if formset.is_valid():
            bus_instances = formset.save()
            bus_ids = [bus_instance.id for bus_instance in bus_instances]
            form = LeadBusForm(request.POST, request.FILES)
            if form.is_valid():
                lead_instance = form.save(commit=False)
                lead_instance.user = request.user
                lead_instance.save()
                m = LeadBus.objects.filter().last()
                m.bus.set(bus_ids)
                return redirect('/leads/')  # Redirect to the leads page
            else:
                return render(request, 'AddBus.html', {'form': form, "bird_formset": formset, 'error': form.errors})

    return render(request, 'AddBus.html', {'form': form, "bird_formset": formset})

def displaybus(request):
    bookings = LeadBus.objects.select_related('leads').prefetch_related('bus')
    return render(request, 'Bus.html', {'bookings': bookings})

def AddTrain(request):
    form = LeadTrainForm()
    formset = TrainFormSet(queryset=Train.objects.none())

    if request.method == 'POST':
        formset = TrainFormSet(request.POST, request.FILES)
        if formset.is_valid():
            train_instances = formset.save()
            train_ids = [train_instance.id for train_instance in train_instances]
            form = LeadTrainForm(request.POST, request.FILES)
            if form.is_valid():
                lead_instance = form.save(commit=False)
                lead_instance.user = request.user
                lead_instance.save()
                m = LeadTrain.objects.filter().last()
                m.train.set(train_ids)
                return redirect('/leads/')  # Redirect to the leads page
            else:
                return render(request, 'AddTrain.html', {'form': form, "bird_formset": formset, 'error': form.errors})

    return render(request, 'AddTrain.html', {'form': form, "bird_formset": formset})

def displayTrain(request):
    bookings = LeadTrain.objects.select_related('leads').prefetch_related('train')
    return render(request, 'Train.html', {'bookings': bookings})

def AddPassport(request):
    form = LeadPassportForm()
    formset = PassportFormSet(queryset=Passport.objects.none())

    if request.method == 'POST':
        formset = PassportFormSet(request.POST, request.FILES)
        if formset.is_valid():
            passport_instances = formset.save()
            passport_ids = [passport_instance.id for passport_instance in passport_instances]
            form = LeadPassportForm(request.POST, request.FILES)
            if form.is_valid():
                lead_instance = form.save(commit=False)
                lead_instance.user = request.user
                lead_instance.save()
                m = LeadPassport.objects.filter().last()
                m.passport.set(passport_ids)
                return redirect('/leads/')  # Redirect to the leads page
            else:
                return render(request, 'AddPassport.html', {'form': form, "bird_formset": formset, 'error': form.errors})

    return render(request, 'AddPassport.html', {'form': form, "bird_formset": formset})

def displayPassport(request):
    bookings = LeadPassport.objects.select_related('leads').prefetch_related('passport')
    return render(request, 'Passport.html', {'bookings': bookings})

def AddCruise(request):
    form = LeadCruiseForm()
    formset = CruiseFormSet(queryset=Flight_booking.objects.none())

    if request.method == 'POST':
        formset = CruiseFormSet(request.POST, request.FILES)
        if formset.is_valid():
            cruise_instances = formset.save()
            cruise_ids = [cruise_instance.id for cruise_instance in cruise_instances]
            form = LeadCruiseForm(request.POST, request.FILES)
            if form.is_valid():
                lead_instance = form.save(commit=False)
                lead_instance.user = request.user
                lead_instance.save()
                m = LeadCruise.objects.filter().last()
                m.cruise.set(cruise_ids)
                return redirect('/leads/')  # Redirect to the leads page
            else:
                return render(request, 'AddCruise.html', {'form': form, "bird_formset": formset, 'error': form.errors})

    return render(request, 'AddCruise.html', {'form': form, "bird_formset": formset})

def displayCruise(request):
    bookings = LeadCruise.objects.select_related('leads').prefetch_related('cruise')
    return render(request, 'Cruise.html', {'bookings': bookings})

def AddAdventure(request):
    form = LeadAdventureForm()
    formset = AdventureFormSet(queryset=Adventure.objects.none())

    if request.method == 'POST':
        formset = AdventureFormSet(request.POST, request.FILES)
        if formset.is_valid():
            adventure_instances = formset.save()
            adventure_ids = [adventure_instance.id for adventure_instance in adventure_instances]
            form = LeadAdventureForm(request.POST, request.FILES)
            if form.is_valid():
                lead_instance = form.save(commit=False)
                lead_instance.user = request.user
                lead_instance.save()
                m = LeadAdventure.objects.filter().last()
                m.adventure.set(adventure_ids)
                return redirect('/leads/')  # Redirect to the leads page
            else:
                return render(request, 'AddAdventure.html', {'form': form, "bird_formset": formset, 'error': form.errors})

    return render(request, 'AddAdventure.html', {'form': form, "bird_formset": formset})

def displayAdventure(request):
    bookings = LeadAdventure.objects.select_related('leads').prefetch_related('adventure')
    return render(request, 'Adventure.html', {'bookings': bookings})   

def AddGroup(request):
    form = LeadGroupForm()
    formset = GroupFormSet(queryset=Group.objects.none())

    if request.method == 'POST':
        formset = GroupFormSet(request.POST, request.FILES)
        if formset.is_valid():
            group_instances = formset.save()
            group_ids = [group_instance.id for group_instance in group_instances]
            form = LeadGroupForm(request.POST, request.FILES)
            if form.is_valid():
                lead_instance = form.save(commit=False)
                lead_instance.user = request.user
                lead_instance.save()
                m = LeadGroup.objects.filter().last()
                m.group.set(group_ids)
                return redirect('/leads/')  # Redirect to the leads page
            else:
                return render(request, 'AddGroup.html', {'form': form, "bird_formset": formset, 'error': form.errors})

    return render(request, 'AddGroup.html', {'form': form, "bird_formset": formset})

def displaygroup(request):
    bookings = LeadGroup.objects.select_related('leads').prefetch_related('group')
    return render(request, 'Group.html', {'bookings': bookings})   


class LeadUpdateView(UpdateView):
    template_name = 'editleads.html'
    model = Lead
    fields = ['customertype','number','email','salutation','firstname','lastname','address','city'
              ,'alternatenumber','alternateemail','leadsource','priority','status','adults','child','infants'
              ,'tags','triptype','assigned','destination','notes','flight_Booking','hotel_Booking','visa','travel_Insurance',
              'forex','sightseeing','transport','other','package','customized_Package','bus','train','passport','cruise','adventure','group']
    success_url ="/leads/"


def delete(Request, id):
    lead = Lead.objects.get(id=id)
    lead.email = Request.POST.get('email')
    lead.delete()
    subject = 'Your Lead is deleted. : Team Travvolt CRM'
    message ="Add other lead with us\nNow You Can Manage Leads :Team Travvolt CRM"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [lead.email, ]
    send_mail(subject, message, email_from, recipient_list)
    return HttpResponseRedirect(reverse('leads'))

def viewlead(Request,id):
    data = Lead.objects.get(id=id)
    return render(Request, "viewlead.html", {"data": data})


#################################### End Lead  ###################################


#################################### Start User  ###################################

def people(Request):
    type = Request.user.type
    if type == "SalesPerson":
        return redirect("/dashboard")
    else:
        data = User.objects.filter(is_internaluser=True)
        print(Request.user)
        return render(Request, "users.html", {'data': data})

class AdduserView(generic.CreateView):
    form_class = UserForm
    template_name = 'adduser.html'
    success_url = reverse_lazy('user')
    
    def form_valid(self,form):
        form.instance.is_internaluser = True
        print(form.instance.id)
        try:
            form.instance.username = str(form.instance.first_name + str(int(random()*10)))
        except:
            form.instance.username =str(form.instance.first_name + str(int(random()*10)))
        return super(AdduserView, self).form_valid(form)
        

def edituser(Request, id):
    data = User.objects.get(id=id)
    if (Request.method == "POST"):
        data.first_name = Request.POST.get('firstname')
        data.last_name = Request.POST.get('lastname')
        data.email = Request.POST.get('email')
        data.contact_no = Request.POST.get('number')
        data.type = Request.POST.get('role')
        data.area = Request.POST.get('area')
        data.save()
        return redirect("/user")
    return render(Request, "edituser.html", {"data": data})

def viewUser(Request,id):
    data = User.objects.get(id=id)
    return render(Request, "viewuser.html", {"data": data})

#################################### End User  ###################################


################################### Start Customer ###################################

def contact(Request):
    # data = customer.objects.all()
    # return render(Request, "contact.html", {'data': data})
    type = Request.user.type
    if type == "Admin":
        data = customer.objects.all()  
    else:
        data = customer.objects.filter(user__email=Request.user.email)
    if Request.method == 'POST':
        salutation = Request.POST.get('salutation')
        firstname = Request.POST.get('firstname')
        lastname = Request.POST.get('lastname')
        number = Request.POST.get('number')
        email = Request.POST.get('email')
        customertype = Request.POST.get('customertype')
        source = Request.POST.get('source')
        tags = Request.POST.get('tags')
        data = customer.objects.filter(Q(salutation=salutation)|Q(firstname=firstname)|Q(lastname=lastname)|Q(number=number)|Q(customertype=customertype)
                            |Q(source=source)|Q(tags=tags)|Q(email=email))
        return render(Request, "contact.html", {'data':data})
    return render(Request, "contact.html", {'data':data})

class CustomerAddView(CreateView):
    form_class = CustomerForm
    template_name = 'addcustomer.html'
    success_url = '/customer/'
    
    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

class CustomerUpdateView(UpdateView):
    template_name = 'editcustomer.html'
    model = customer
    fields = ['number','email','salutation','firstname','lastname','address','address2','city'
              ,'pincode','alternateaddress','alternatemobile','alternateemail','source','customertype'
              ,'accounthead','tags','flyer','food','pan','passport','enquirydate','issuedate']
    success_url ="/customer/"



def viewcustomer(Request,id):
    d = customer.objects.get(id=id)
    return render(Request, "viewcustomer.html", {"d": d})

################################### End Customer  ##############################################

###################################  Start Supplier ##############################################

def Supplier(Request):
    type = Request.user.type
    if type == "Admin":
        data = supplier.objects.all()  
    else:
        data = supplier.objects.filter(user__email=Request.user.email)
    return render (Request,"supplier.html",{'suppliers':data})

def viewsupplier(Request,id):
    s = supplier.objects.get(id=id)
    return render(Request, "viewsupplier.html", {"s": s})


class SupplierAddView(CreateView):
    form_class = SupplierForm
    template_name = 'addsupplier.html'
    success_url = '/supplier/'
    
    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

class SupplierUpdateView(UpdateView):
    template_name = 'editsupplier.html'
    model = supplier
    fields = ['company_name','alias_name','gst_no','billing_address','city','visa','flights','hotel'
              ,'travel_insurance','forex','sightseeing','cruise','transport','other','package','customize_package'
              ,'bus','train','passport','adventure','group_package','country','tags','name','designation','number','email'
              ,'alternate_number','alternate_email','preffered_supplier','inactive_supplier','default_email','cc_email','bank_details','note']
    success_url ="/supplier/"

##################################### End Supplier ##############################################


################################### Start Sightseeing ##############################################

def sightseeing(Request):
    type = Request.user.type
    if type == "Admin":
        data = Sightseeing.objects.all()  
    else:
        data = Sightseeing.objects.filter(user__email=Request.user.email)
        if Request.method == 'POST':
            country = Request.POST.get('country')
            city = Request.POST.get('city')
            data = Sightseeing.objects.filter(Q(country=country)|Q(city=city))
            return render(Request,'sightseeing.html',{'sightseen':data})
    return render(Request,'sightseeing.html',{'sightseen':data})

class SightseeingAddView(CreateView):
    form_class = SightseeingForm
    template_name = 'addsightseeing.html'
    success_url = '/sightseeing/'
    
    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

class SightseeingUpdateView(UpdateView):
    template_name = 'editsightseeing.html'
    model = Sightseeing
    fields = ['country','city','activity','description','inclusion','exclusion','duration','close_day'
              ,'timings','transport','time','remark','internal_remark','external_remark','image']
    success_url ="/sightseeing/"

def viewsightseeing(Request,id):
    s = Sightseeing.objects.get(id=id)
    return render(Request, "viewsightseeing.html", {"s": s})

################################ End Sightseeing ##############################################


############################### Start Transport ##############################################

def transport(Request):
    type = Request.user.type
    if type == "Admin":
        transport = Vehicle.objects.all()
    else:
        transport = Vehicle.objects.filter(user__email = Request.user.email)
    if Request.method == 'POST':
        country = Request.POST.get('country')
        city = Request.POST.get('city')
        transport = Vehicle.objects.filter(Q(country=country)|Q(city=city))
        return render(Request,"transport.html",{'transport':transport})
    return render(Request,'transport.html',{'transport':transport})
    
    
    
class TransportAddView(CreateView):
    form_class = VehicleForm
    template_name = 'addtransport.html'
    success_url = '/transport/'
    
    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

class TransportUpdateView(UpdateView):
    template_name = 'edittransport.html'
    model = Vehicle
    fields = ['country','city','vehicle_type','title','description','internal_remark','image']
    success_url ="/transport/"

def viewtransport(Request,id):
    t = Vehicle.objects.get(id=id)
    return render(Request,"viewtransport.html",{'t':t})

################################### End Transport ###################################


################################### Start Packages ###################################

def packages(Request):
    type = Request.user.type
    if type == "Admin":
        data = Package.objects.all()  
    else:
        data = Package.objects.filter(created_by__email=Request.user.email)
    if Request.method == "POST":
        country = Request.POST.get('country')

        data = Package.objects.filter(Q(country=country))
        return render(Request, "packages.html", {"p2": data})
    return render(Request, "packages.html", {"p2": data})


def addpackages(request):
    form = PackageForm()
    formset = BirdFormSet(queryset=Destination.objects.none())

    
    if request.method == 'POST':
        formset = BirdFormSet(request.POST)
        
        
        if formset.is_valid():
            list=[]
            for i in formset:
                inst = i.save()
                list.append(inst.id)
        
        form = PackageForm(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.created_by=request.user
            instance.save()
            m = Package.objects.filter(created_by= request.user).last()
            m.destinations.set(list)
            
        else:
            print("form.errors:",form.errors)
    return render(request, 'addpackages.html', {'form': form,"bird_formset": formset})


class BirdAddView(TemplateView):
    template_name = "addpackages.html"

    def get(self, *args, **kwargs):
        formset = BirdFormSet(queryset=Destination.objects.none())
        form = PackageForm()
        return self.render_to_response({"bird_formset": formset,'form':form})

    def post(self, *args, **kwargs):

        formset = BirdFormSet(data=self.request.POST)

        if formset.is_valid():
           instance2=formset.save()
        form = PackageForm(data=self.request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.created_by=self.request.user
            instance.save()
            m = Package.objects.filter(created_by= self.request.user).last()
            m.destinations.add(instance2.id)
            return redirect(reverse_lazy("bird_list"))

        return self.render_to_response({"bird_formset": formset})


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

class GenerateInvoice(View):
    def get(self, request,id, *args, **kwargs):
        order_db = Package.objects.get(created_by=request.user.id,id=id)

        data = {
            'Package_name': order_db.package_name,
            'Country': order_db.country,
            'Destinations':order_db.destinations.all(),
            'Days':order_db.days,
            'Detailed_Itenerary':order_db.detailed_itenerary,
            'Hotel_Details':order_db.hotel_details,
            'Tags':order_db.tags,
            'Meal_Type': order_db.meal_type,
            'Free_WiFi':order_db.free_wi_fi,
            'Airport_Transfers_Private':order_db.airport_transfers_private,
            'Airport_Transfers_SIC':order_db.airport_transfers_sic,
            'Travel_Insurance':order_db.travel_insurance,
            'Visa':order_db.visa,
            'Inter_Hotel_Transfer_Private':order_db.Inter_hotel_transfer_private,
            'Sightseeing_Transfer_Private':order_db.sightseeing_transfer_private,
            'Sightseeing_Transfer_SIC':order_db.sightseeing_transfer_sic,
            'Inter_Hotel_Transfer_SIC':order_db.Inter_hotel_transfer_sic,
            'Candle_Light_Dinner':order_db.candlelight_dinner,
            'Bed_Decorations':order_db.bed_decorations,
            'Honeymoon_Cake':order_db.honeymoon_cake,
            'Private_Ferry':order_db.private_ferry,
            'Private_Cruise':order_db.private_cruise,
            'Scuba_Diving':order_db.scuba_diving,
            'Parasailing':order_db.parasailing,            
            'Sea_Walk':order_db.sea_walk,              
            'Photoshoot_for_Couple':order_db.photoshoot_for_couple,            
            'Candle_Light_Dinner_With_Wine':order_db.candle_light_dinner_with_wine,            
            'Candle_Light_Dinner_Without_Wine':order_db.candle_light_dinner_without_wine,            
            'Jet_Ski':order_db.jet_ski,            
            'Snorkeling':order_db.snorkeling,            
            'Airport_Transfers_Speed_Boat_Sea_Plane':order_db.airport_transfers_speed_boat_seaplane,    
            'Inclusive':order_db.inclusive,
            'Exclusive':order_db.exclusive,
            'Terms_and_Conditions':order_db.terms_and_conditions,
            'Cancellation_Policy':order_db.cancellation_policy,
            'Image': order_db.image,
           
            
            
        }
        pdf = render_to_pdf('packagereciept_pdf.html', data)
        

        # pdf download
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = f"Invoice_{order_db.id}.pdf"
            content = "inline; filename='%s'" %(filename)
            content = "attachment; filename=%s" %(filename)
            response['Content-Disposition'] = content
       
            return response
        return HttpResponse("Not found")

def viewpackages(Request, id):
    data = Package.objects.get(id=id)
    return render(Request, "viewpackages.html", {"p2": data})


class PackageUpdateView(UpdateView):
    template_name = 'editpackages.html'
    model = Package
    fields = ['package_name','country','days','detailed_itenerary','hotel_details',
              'tags','meal_type','free_wi_fi','airport_transfers_private','airport_transfers_sic',
              'travel_insurance','visa','Inter_hotel_transfer_private','sightseeing_transfer_private',
              'sightseeing_transfer_sic','Inter_hotel_transfer_sic','candlelight_dinner','bed_decorations',
              'honeymoon_cake','private_ferry','private_cruise','scuba_diving','parasailing','sea_walk',
              'photoshoot_for_couple','candle_light_dinner_with_wine','candle_light_dinner_without_wine',
              'jet_ski','snorkeling','airport_transfers_speed_boat_seaplane','image','inclusive','exclusive',
              'terms_and_conditions','cancellation_policy']
    success_url ="/packages/"


################################### End Package ########################################


################################### Start Hotel ######################################

def hotels(Request):
    type = Request.user.type
    if type == "Admin":
        data = Hotel.objects.all()  
    else:
        data = Hotel.objects.filter(user__email=Request.user.email)
    if Request.method == "POST":
        country = Request.POST.get('country')
        city = Request.POST.get('city')

        data = Hotel.objects.filter(Q(country=country) | Q(city=city))
        return render(Request, "hotels.html", {"h2": data})
    return render(Request, "hotels.html", {"h2": data})

class HotelAddView(CreateView):
    form_class = HotelForm
    template_name = 'addhotels.html'
    success_url = '/hotels/'
    
    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

class HotelUpdateView(UpdateView):
    template_name = 'edithotels.html'
    model = Hotel
    fields = ['hotel_name','country','city','address','contact','email','rate','hotel_type'
              ,'child_freeage','child_without_freeage','amenities','description','image']
    success_url ="/hotels/"

def viewhotels(Request,id): 
    data = Hotel.objects.get(id=id)
    return render(Request, "viewhotels.html", {"h1": data})

################################### End Hotel ##############################################



def visa(Request):
    return render(Request,"visainfo.html")

def addvisa(Request):
    return render(Request,"addvisa.html")


#################################### Creating the RestAPI  ###################################

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def lead_api(Request, pk=None): 
    if Request.method == 'GET':
        id = pk 
        if id is not None:
            lead = Lead.objects.get(id=id)
            serializer = LeadModelSerializer(lead)
            return Response(serializer.data)
        
        lead = Lead.objects.all()
        serializer = LeadModelSerializer(lead, many=True)
        return Response(serializer.data)
    
    if Request.method == 'POST':
        serializer = LeadModelSerializer(data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Lead is Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'PUT':
        id = pk
        lead = Lead.objects.get(pk=id)
        serializer = LeadModelSerializer(lead, data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete data Updated'}, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'PATCH':
        id = pk 
        lead = Lead.objects.get(pk=id)
        serializer = LeadModelSerializer(lead, data=Request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'}, status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'DELETE':
        id = pk 
        lead = Lead.objects.get(pk=id)
        lead.delete()
        return Response({'msg':'Data Deleted'}, status=status.HTTP_301_MOVED_PERMANENTLY)
    

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def customer_api(Request, pk=None):
    if Request.method == 'GET':
        id = pk 
        if id is not None:
            Customer = customer.objects.get(id=id)
            serializer = CustomerModelSerializer(Customer)
            return Response(serializer.data)
        
        Customer = customer.objects.all()
        serializer = CustomerModelSerializer(Customer, many=True)
        return Response(serializer.data)
    
    if Request.method == 'POST':
        serializer = CustomerModelSerializer(data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Customer is Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'PUT':
        id = pk
        Customer = customer.objects.get(pk=id)
        serializer = CustomerModelSerializer(Customer, data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete data Updated'}, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'PATCH':
        id = pk 
        Customer = customer.objects.get(pk=id)
        serializer = CustomerModelSerializer(customer, data=Request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'}, status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'DELETE':
        id = pk 
        Customer = customer.objects.get(pk=id)
        Customer.delete()
        return Response({'msg':'Data Deleted'}, status=status.HTTP_301_MOVED_PERMANENTLY)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def supplier_api(Request, pk=None):
    if Request.method == 'GET':
        id = pk 
        if id is not None:
            Supplier = supplier.objects.get(id=id)
            serializer = SupplierModelSerializer(Supplier)
            return Response(serializer.data)
        
        Supplier = supplier.objects.all()
        serializer = SupplierModelSerializer(Supplier, many=True)
        return Response(serializer.data)
    
    if Request.method == 'POST':
        serializer = SupplierModelSerializer(data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Supplier is Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'PUT':
        id = pk
        Supplier = supplier.objects.get(pk=id)
        serializer = SupplierModelSerializer(Supplier, data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete data Updated'}, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'PATCH':
        id = pk 
        Supplier = supplier.objects.get(pk=id)
        serializer = SupplierModelSerializer(Supplier, data=Request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'}, status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'DELETE':
        id = pk 
        Supplier = supplier.objects.get(pk=id)
        Supplier.delete()
        return Response({'msg':'Data Deleted'}, status=status.HTTP_301_MOVED_PERMANENTLY)
    
    
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def sightseeing_api(Request, pk=None):
    if Request.method == 'GET':
        id = pk 
        if id is not None:
            sightseeing = Sightseeing.objects.get(id=id)
            serializer = SightseeingModelSerializer(sightseeing)
            return Response(serializer.data)
        
        sightseeing = Sightseeing.objects.all()
        serializer = SightseeingModelSerializer(sightseeing, many=True)
        return Response(serializer.data)
    
    if Request.method == 'POST':
        serializer = SightseeingModelSerializer(data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Sightseeing is Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'PUT':
        id = pk
        sightseeing = Sightseeing.objects.get(pk=id)
        serializer = SightseeingModelSerializer(Supplier, data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete data Updated'}, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'PATCH':
        id = pk 
        sightseeing = supplier.objects.get(pk=id)
        serializer = SightseeingModelSerializer(Supplier, data=Request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'}, status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'DELETE':
        id = pk 
        sightseeing = Sightseeing.objects.get(pk=id)
        sightseeing.delete()
        return Response({'msg':'Data Deleted'}, status=status.HTTP_301_MOVED_PERMANENTLY)
    

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def package_api(Request, pk=None):
    if Request.method == 'GET':
        id = pk 
        if id is not None:
            package = Package.objects.get(id=id)
            serializer = PackageModelSerializer(package)
            return Response(serializer.data)
        
        package = Package.objects.all()
        serializer = PackageModelSerializer(package, many=True)
        return Response(serializer.data)
    
    if Request.method == 'POST':
        serializer = PackageModelSerializer(data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Package is Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'PUT':
        id = pk
        package = Package.objects.get(pk=id)
        serializer = PackageModelSerializer(package, data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete data Updated'}, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'PATCH':
        id = pk 
        package = Package.objects.get(pk=id)
        serializer = PackageModelSerializer(package, data=Request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'}, status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'DELETE':
        id = pk 
        package = Package.objects.get(pk=id)
        package.delete()
        return Response({'msg':'Data Deleted'}, status=status.HTTP_301_MOVED_PERMANENTLY)
    

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def vehicle_api(Request, pk=None):
    if Request.method == 'GET':
        id = pk 
        if id is not None:
            vehicle = Vehicle.objects.get(id=id)
            serializer = VehicleModelSerializer(vehicle)
            return Response(serializer.data)
        
        vehicle = Vehicle.objects.all()
        serializer = VehicleModelSerializer(vehicle, many=True)
        return Response(serializer.data)
    
    if Request.method == 'POST':
        serializer = VehicleModelSerializer(data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Transportation detail is Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'PUT':
        id = pk
        vehicle = Vehicle.objects.get(pk=id)
        serializer = VehicleModelSerializer(data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete data Updated'}, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'PATCH':
        id = pk 
        vehicle = Vehicle.objects.get(pk=id)
        serializer = VehicleModelSerializer(vehicle, data=Request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'}, status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'DELETE':
        id = pk 
        vehicle = Vehicle.objects.get(pk=id)
        vehicle.delete()
        return Response({'msg':'Data Deleted'}, status=status.HTTP_301_MOVED_PERMANENTLY)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def hotel_api(Request, pk=None):
    if Request.method == 'GET':
        id = pk 
        if id is not None:
            hotel = Hotel.objects.get(id=id)
            serializer = HotelModelSerializer(hotel)
            return Response(serializer.data)
        
        hotel = Hotel.objects.all()
        serializer = HotelModelSerializer(hotel, many=True)
        return Response(serializer.data)
    
    
    if Request.method == 'POST':
        serializer = HotelModelSerializer(data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Hotels detail is Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
    
    if Request.method == 'PUT':
        id = pk
        hotel = Hotel.objects.get(pk=id)
        serializer = HotelModelSerializer(data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete data Updated'}, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    if Request.method == 'PATCH':
        id = pk 
        hotel = Hotel.objects.get(pk=id)
        serializer = HotelModelSerializer(hotel, data=Request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'}, status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    if Request.method == 'DELETE':
        id = pk 
        hotel = Hotel.objects.get(pk=id)
        hotel.delete()
        return Response({'msg':'Data Deleted'}, status=status.HTTP_301_MOVED_PERMANENTLY)

    
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def user_api(Request, pk=None):
    if Request.method == 'GET':
        id = pk 
        if id is not None:
            user = User.objects.get(id=id)
            serializer = UserModelSerializer(user)
            return Response(serializer.data)
        
        user = User.objects.all()
        serializer = UserModelSerializer(user, many=True)
        return Response(serializer.data)
    
    if Request.method == 'POST':
        serializer = UserModelSerializer(data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'User is Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'PUT':
        id = pk
        user = User.objects.get(pk=id)
        serializer = UserModelSerializer(data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete data Updated'}, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'PATCH':
        id = pk 
        user = User.objects.get(pk=id)
        serializer = UserModelSerializer(user, data=Request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'}, status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if Request.method == 'DELETE':
        id = pk 
        user = User.objects.get(pk=id)
        user.delete()
        return Response({'msg':'Data Deleted'}, status=status.HTTP_301_MOVED_PERMANENTLY)


################################### End APIs ######################################################


