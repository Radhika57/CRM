from django.contrib import admin
from .models import *
    
class LeadAdmin(admin.ModelAdmin):
    list_display = ['leadno','customertype','number','email','salutation','firstname','lastname']
    
class FlightbookingAdmin(admin.ModelAdmin):
    list_display=['dep_from','dep_to']
    
class HotelBookingAdmin(admin.ModelAdmin):
    list_display=['hcountry','hcity','Hotelname']
    
class VisaAdmin(admin.ModelAdmin):
    list_display=['country','visa_category']
    
class TravelInsuranceAdmin(admin.ModelAdmin):
    list_display=['country','how_long','travel_date']
    
class ForexAdmin(admin.ModelAdmin):
    list_display=['currency','amount']
    
class SightseenAdmin(admin.ModelAdmin):
    list_display=['country','city','sightseen_options']
    
class TransportAdmin(admin.ModelAdmin):
    list_display=['country','city']
    
class OtherAdmin(admin.ModelAdmin):
    list_display=['country','travel_date','no_of_days']
  
class PackageeAdmin(admin.ModelAdmin):
    list_display=['travel_date','budget']
    
class CustomizedPacakgeAdmin(admin.ModelAdmin):
    list_display=['country','service','rating']
    
class BusAdmin(admin.ModelAdmin):
    list_display=['country','From','to']
    
class TrainAdmin(admin.ModelAdmin):
    list_display=['country','From','to']
    
class PassportAdmin(admin.ModelAdmin):
    list_display=['country','date','no_of_person']
  
class CruiseAdmin(admin.ModelAdmin):
    list_display=['country','City']
    
class AdventureAdmin(admin.ModelAdmin):
    list_display=['country','city','travel_date']
    
class GroupAdmin(admin.ModelAdmin):
    list_display=['country','package_name','preference']
  
class customerAdmin(admin.ModelAdmin):
    list_display = ['number','email','salutation','firstname','lastname','address','address2','city']

class supplierAdmin(admin.ModelAdmin):
    list_display=['company_name','alias_name','name','number','email']
   
class sightseeingAdmin(admin.ModelAdmin):
    list_display=['country','city','activity','duration','image'] 
    
class VehicleAdmin(admin.ModelAdmin):
    list_display=['country','city','vehicle_type'] 
    
class HotelAdmin(admin.ModelAdmin):
    list_display = ['hotel_name','country','city','address','contact','email','rate','hotel_type']

class DestinationAdmin(admin.ModelAdmin):
    list_display=['destination'] 
    
    
class PackageAdmin(admin.ModelAdmin):
    raw_id_fields = ['destinations']
    list_display = ['package_name','country','tags','overview','meal_type','image','inclusive','exclusive']

class WhatsappAdmin(admin.ModelAdmin):
    list_display = ['number']

admin.site.register(Lead,LeadAdmin)
admin.site.register(Flight_booking,FlightbookingAdmin)
admin.site.register(Hotel_booking,HotelBookingAdmin)
admin.site.register(Visa_booking,VisaAdmin)
admin.site.register(Travel_insurance,TravelInsuranceAdmin)
admin.site.register(Forex,ForexAdmin)
admin.site.register(Sightseen,SightseenAdmin)
admin.site.register(Transport,TransportAdmin)
admin.site.register(Other,OtherAdmin)
admin.site.register(Packagee,PackageeAdmin)
admin.site.register(Customized_Package,CustomizedPacakgeAdmin)
admin.site.register(Bus,BusAdmin)
admin.site.register(Train,TrainAdmin)
admin.site.register(Passport,PassportAdmin)
admin.site.register(Cruise,CruiseAdmin)
admin.site.register(Adventure,AdventureAdmin)
admin.site.register(Group,GroupAdmin)
admin.site.register(customer,customerAdmin)
admin.site.register(supplier,supplierAdmin)
admin.site.register(Sightseeing,sightseeingAdmin)
admin.site.register(Vehicle,VehicleAdmin)
admin.site.register(Hotel,HotelAdmin)
admin.site.register(Package,PackageAdmin)
admin.site.register(Destination,DestinationAdmin)
admin.site.register(WhatsAppNumber,WhatsappAdmin)
admin.site.register(FlightBooking)
admin.site.register(HotelBooking)
admin.site.register(VisaBooking)
admin.site.register(TravelInsurance)
admin.site.register(LeadForex)
admin.site.register(LeadSightseen)
admin.site.register(LeadTransport)
admin.site.register(LeadOther)
admin.site.register(LeadPackage)
admin.site.register(CustomizedPackage)
admin.site.register(LeadBus)
admin.site.register(LeadTrain)
admin.site.register(LeadPassport)
admin.site.register(LeadCruise)
admin.site.register(LeadAdventure)
admin.site.register(LeadGroup)
