# forms.py
from django import forms
from .models import *
from django.forms import modelformset_factory
from django.forms import inlineformset_factory


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = "__all__"
        exclude = ['leadno']
        
    def __init__(self, *args, **kwargs):
        super(LeadForm, self).__init__(*args, **kwargs)
        self.fields['customertype'].label = 'Customer Type'
        self.fields['number'].label = 'Mobile Number'
        self.fields['email'].label = 'Email Id'
        self.fields['firstname'].label = 'First Name'
        self.fields['lastname'].label = 'Last Name'
        self.fields['alternatenumber'].label = 'Alternate Mobile Number'
        self.fields['alternateemail'].label = 'Alternate Email Id'
        self.fields['leadsource'].label = 'Lead Source'
        self.fields['priority'].label = 'Lead Priority'
        self.fields['status'].label = 'Lead Status'
        self.fields['adults'].label = 'No of Adults'
        self.fields['child'].label = 'No of Children'
        self.fields['infants'].label = 'No of Infants'
        self.fields['triptype'].label = 'Trip Type'
        self.fields['assigned'].label = 'Assigned To'

class FlightBookingForm(forms.ModelForm):
    class Meta:
        model = Flight_booking
        fields = "__all__"
        
FlightFormSet = modelformset_factory(Flight_booking, fields=('dep_from','dep_to','departure','return_to','classes','domestic_flight','internation_flight','flexibility','preference',), extra=1)

class LeadFlightForm(forms.ModelForm):
    class Meta:
        model = FlightBooking
        exclude = ["flight"]
        
class HotelBookingForm(forms.ModelForm):
    class Meta:
        model = Hotel_booking
        fields = "__all__"
        
HotelFormSet = modelformset_factory(Hotel_booking, fields=('hcountry','hcity','checkin','checkout','roomtype','rating','nights','budget','Hotelname','rooms',), extra=1)

class LeadHotelForm(forms.ModelForm):
    class Meta:
        model = HotelBooking
        exclude = ["hotel"]
        
class VisaBookingForm(forms.ModelForm):
    class Meta:
        model = Visa_booking
        fields = "__all__"
        
VisaFormSet = modelformset_factory(Visa_booking, fields=('country','visa_category','visit_type','duration','traveldate','job_profile','age','qualification','description',), extra=1)

class LeadVisaForm(forms.ModelForm):
    class Meta:
        model = VisaBooking
        exclude = ["visa"]
        
class Travel_insuranceForm(forms.ModelForm):
    class Meta:
        model = Travel_insurance
        fields = "__all__"
        
TravelFormSet = modelformset_factory(Travel_insurance, fields=('country','how_long','travel_date','insurace',), extra=1)

class LeadTravelForm(forms.ModelForm):
    class Meta:
        model = TravelInsurance
        exclude = ["travelinsurance"]
        
class ForexForm(forms.ModelForm):
    class Meta:
        model = Forex
        fields = "__all__"
        
ForexFormSet = modelformset_factory(Forex, fields=('currency','amount',), extra=1)

class LeadForexForm(forms.ModelForm):
    class Meta:
        model = LeadForex
        exclude = ["forex"]
        
class SightseenForm(forms.ModelForm):
    class Meta:
        model = Sightseen
        fields = "__all__"
        
SightseenFormSet = modelformset_factory(Sightseen, fields=('country','city','sightseen_options','preference','travel_date',), extra=1)

class LeadSightseenForm(forms.ModelForm):
    class Meta:
        model = LeadSightseen
        exclude = ["sightseen"]
        
class TransportForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = "__all__"
        
TransportFormSet = modelformset_factory(Transport, fields=('country','city','trasport_date','drop_date','preference','Airport_transfers','Sightseeing_transfers','Others',), extra=1)

class LeadTransportForm(forms.ModelForm):
    class Meta:
        model = LeadTransport
        exclude = ["transport"]
        
class OtherForm(forms.ModelForm):
    class Meta:
        model = Other
        fields = "__all__"
        
OtherFormSet = modelformset_factory(Other, fields=('country','travel_date','no_of_days','sub_category','description',), extra=1)

class LeadOtherForm(forms.ModelForm):
    class Meta:
        model = LeadOther
        exclude = ["other"]
        
class PackageeForm(forms.ModelForm):
    class Meta:
        model = Packagee
        fields = "__all__"
        
PackageeFormSet = modelformset_factory(Packagee, fields=('travel_date','budget','country','package_name','extra_details',), extra=1)

class LeadPackageForm(forms.ModelForm):
    class Meta:
        model = LeadPackage
        exclude = ["package"]
        
class CustomizedPackageForm(forms.ModelForm):
    class Meta:
        model = Customized_Package
        fields = "__all__"
        
CustomizedPackageFormSet = modelformset_factory(Customized_Package, fields=('country','service','rating','travel_date','no_of_night','flexibility','no_of_rooms','preferance','budget','description',), extra=1)

class LeadCustomizedPackageForm(forms.ModelForm):
    class Meta:
        model = CustomizedPackage
        exclude = ["customizedpackage"]
        
class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = "__all__"
        
BusFormSet = modelformset_factory(Bus, fields=('country','From','to','departure','Return','preference','remark',), extra=1)

class LeadBusForm(forms.ModelForm):
    class Meta:
        model = LeadBus
        exclude = ["bus"]
        
class TrainForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = "__all__"
        
TrainFormSet = modelformset_factory(Train, fields=('country','From','to','departure','Return','preference','remark',), extra=1)

class LeadTrainForm(forms.ModelForm):
    class Meta:
        model = LeadTrain
        exclude = ["train"]
        
class PassportForm(forms.ModelForm):
    class Meta:
        model = Passport
        fields = "__all__"
        
PassportFormSet = modelformset_factory(Passport, fields=('country','date','passport_no','place_of_apply','no_of_person','new_passport','renew_passport','urgent','remark',), extra=1)

class LeadPassportForm(forms.ModelForm):
    class Meta:
        model = LeadPassport
        exclude = ["passport"]
        
class CruiseForm(forms.ModelForm):
    class Meta:
        model = Cruise
        fields = "__all__"
        
CruiseFormSet = modelformset_factory(Cruise, fields=('country','City','days','Cruise_name','type','departure','Return','room_type','remark',), extra=1)

class LeadCruiseForm(forms.ModelForm):
    class Meta:
        model = LeadCruise
        exclude = ["cruise"]
        
class AdventureForm(forms.ModelForm):
    class Meta:
        model = Adventure
        fields = "__all__"
        
AdventureFormSet = modelformset_factory(Adventure, fields=('country','city','travel_date','motorbiking','camping','safari','water_sports','remark',), extra=1)

class LeadAdventureForm(forms.ModelForm):
    class Meta:
        model = LeadAdventure
        exclude = ["adventure"]
        
class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = "__all__"
        
GroupFormSet = modelformset_factory(Group, fields=('country','package_name','preference','remark',), extra=1)

class LeadGroupForm(forms.ModelForm):
    class Meta:
        model = LeadGroup
        exclude = ["group"]

   
class SupplierForm(forms.ModelForm):
    class Meta:
        model=supplier
        # fields = "__all__"
        exclude = ["user"]
        
        
        
class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        # fields = "__all__"
        exclude = ('created_by','destinations')
        class Meta:
            widgets = {
                'mealtype' : forms.ChoiceField(choices=Type_of_Tags, widget=forms.RadioSelect()),
        }
            
        


# A regular form, not a formset
class BirdForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ["destination"]


BirdFormSet = modelformset_factory(Destination, fields=("destination",), extra=1)


class CustomerForm(forms.ModelForm):
    class Meta:
        model=customer
        # fields = "__all__"
        exclude = ["user"]
        
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['number'].label = 'Mobile Number'
        self.fields['email'].label = 'Email Id'
        self.fields['source'].label = 'Contact Source'
        self.fields['tags'].label = 'Add Tag'
        self.fields['flyer'].label = 'Frequent Flyer'
        self.fields['food'].label = 'Food Prefrence'
        self.fields['pan'].label = 'Pan Number'
        self.fields['passport'].label = 'Passport Number'
        self.fields['enquirydate'].label = 'Passport Enquiry Date'
        self.fields['issuedate'].label = 'Passport Issue Date'

class HotelForm(forms.ModelForm):
    class Meta:
        model=Hotel
        # fields = "__all__"
        exclude = ["user"]
        
    def __init__(self, *args, **kwargs):
        super(HotelForm, self).__init__(*args, **kwargs)
        self.fields['rate'].label = 'Star Rating'
        self.fields['contact'].label = 'Phone No.'
        self.fields['child_freeage'].label = 'Child Free Age - No charges till this age'
        self.fields['child_without_freeage'].label = 'Child Without Free Age - Without Free charges till this age'
        
class SightseeingForm(forms.ModelForm):
    class Meta:
        model=Sightseeing
        # fields = "__all__"
        exclude = ["user"] 
        
    def __init__(self, *args, **kwargs):
        super(SightseeingForm, self).__init__(*args, **kwargs)
        self.fields['timings'].label = 'Timings (Open-Close)'
        self.fields['time'].label = 'Start Time'
        

class VehicleForm(forms.ModelForm):
    class Meta:
        model=Vehicle
        # fields = "__all__"
        exclude = ["user"]
        

