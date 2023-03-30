from django.db import models
from . utils import generate_lead_no
from Useraccount.models import User
from django.utils import timezone
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django import forms
    
Type_of_customer = (
    ('B2B','B2B'),
    ('B2C','B2C'),
    ('Corporate','Corporate'),
    ('VIP','VIP'),
)    

Type_of_days = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10')

) 

Type_of_salutation = (
    ('Mr','Mr'),
    ('Mrs','Mrs'),
    ('Miss','Miss'),
    ('Dr','Dr'),
)

Type_of_Leadsource = (
    ('Advertisement','Advertisement'),
    ('Cold Call','Cold Call'),
    ('Employee Referral','Employee Referral'),
    ('External Referral','External Referral'),
    ('Website','Website'),
    ('Public Relation','Public Relation'),
    ('Email Campaign','Email Campaign'),
    ('SMS Campaign','SMS Campaign'),
    ('Trade Show','Trade Show'),
    ('None','None'),
    ('Old Customer','Old Customer'),
    ('New Customer','New Customer'),
    ('Walk In','Walk In'),
    ('SEO','SEO'),
    ('Excel','Excel'),
    ('Just Dial','Just Dial'),
    ('Phone Call','Phone Call'),
    ('Airbnb','Airbnb'),
    ('Live Chat','Live Chat'),
    ('Travvolt','Travvolt'),
    ('Hello Travel','Hello Travel'),
    ('TripShelf','TripShelf'),
    ('Newspaper','Newspaper'),
    ('Sulekha','Sulekha'),
    ('Travel Triangle','Travel Triangle'),
    ('TripCrafters','TripCrafters'),
    ('Other','Other'),
    ('Flyer','Flyer'),
    ('Travelsetu','Travelsetu'),
    ('Facebook','Facebook'),
    ('Google Ads','Google Ads'),
    ('Instagram','Instagram'),
    ('10Times','10Times'),
    ('Rotary','Rotary'),
    ('BNI','BNI'),
    ('YES','YES'),
    ('Mail','Mail'),
    ('Agent','Agent'),
    ('Google','Google'),
    ('Whatsapp','Whatsapp'),
    ('Webmail','Webmail'),
    ('Direct Sales','Direct Sales'),
    ('Incoming Call','Incoming Call'),
    ('Chat','Chat'),
    ('Brouchers','Brouchers'),
)

Type_of_leadpriority = (
    ('All','All'),
    ('Cold','Cold'),
    ('Warm','Warm'),
    ('Hot','Hot'),
)

Type_of_leadstatus = (
    ('All','All'),
    ('Unquilified','Unquilified'),
    ('New','New'),
    ('Working','Working'),
    ('Proposal Sent','Proposal Sent'),
    ('Negotiating','Negotiating'),
    ('Booked','Booked'),
    ('Lost','Lost'),
)

Type_of_Tags = (
    ('All','All'),
    ('Family','Family'),
    ('Honeymoon','Honeymoon'),
    ('Individual','Individual'),
    ('Adventure','Adventure'),
    ('Group','Group'),
    ('Women Only','Women Only'),
    ('Domestic','Domestic'),
    ('International','International'),
    ('Beaches','Beaches'),
    ('Weekend','Weekend'),
    ('Heritage','Heritage'),
    ('Wildlife','Wildlife'),
    ('Jungle Safari','Jungle Safari'),
    ('Student','Student'),
    ('Pilgrimage','Pilgrimage'),
    ('Popular','Popular'),
    ('Trending','Trending'),
)

Type_of_Trip = (
    ('Other','Other'),
    ('Family','Family'),
    ('Honeymoon','Honeymoon'),
    ('Friends','Friends'),
    ('Official','Official'),
    ('Adventure','Adventure'),
    ('Corporate','Corporate'),
    ('Educational','Educational'),
    ('Group','Group'),
    ('Individual','Individual'),
    ('Religious','Religious'),
    ('Couple','Couple'),
    ('Student Group','Student Group'),
)

Type_of_food = (
    ('All','All'),
    ('Vegetarian','Vegetarian'),
    ('NonVegetarian','NonVegetarian'),
    ('Jainism','Jainism'),
    ('Sweet','Sweet')
)

Type_of_vehicle= (
    ('Sedan', 'Sedan'),
    ('Hatchback', 'Hatchback'),
    ('MPV', 'MPV'),
    ('SUV', 'SUV'),
)

Type_of_Transport=(
    ('Private','Private'),
    ('SIC','SIC'),
    ('Other','Other'),
)

class Lead(models.Model):
    leadno = models.CharField(max_length=50)
    # user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_lead')
    customertype = models.CharField(max_length=100,choices=Type_of_customer,default='B2B') 
    number = PhoneNumberField(max_length=20)
    email = models.EmailField(max_length=100)
    salutation = models.CharField(max_length=100,choices=Type_of_salutation,default='Mr') 
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=500,blank=True,null=True)
    city = models.CharField(max_length=100)
    alternatenumber = models.CharField(max_length=15,blank=True,null=True)
    alternateemail = models.EmailField(max_length=100,blank=True,null=True)
    leadsource = models.CharField(max_length=100,null=True,choices=Type_of_Leadsource,default='Advertisement') 
    priority = models.CharField(max_length=100,choices=Type_of_leadpriority,default='All') 
    status = models.CharField(max_length=100,null=True,choices=Type_of_leadstatus,default='All') 
    adults = models.IntegerField(blank=True)
    child = models.CharField(max_length=15,blank=True,null=True)
    infants = models.CharField(max_length=15,blank=True,null=True)
    tags = models.CharField(max_length=100,null=True,choices=Type_of_Tags,default='All')   
    triptype = models.CharField(max_length=100,null=True,choices=Type_of_Trip,default='Other') 
    assigned = models.ForeignKey(User,on_delete=models.CASCADE) 
    destination = models.CharField(max_length=100,blank=True,null=True,default='-')
    created = models.DateTimeField(editable=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # enquirytype = models.CharField(max_length=100)
    
    def save(self, *args, **kwargs):
        if self.leadno =="":
            lead_no = (generate_lead_no())
            
            self.leadno=lead_no
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.firstname)
    
class customer(models.Model): 
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_customer')
    number = PhoneNumberField(max_length=20,null=True)
    email = models.EmailField(max_length=100,blank=True,null=True)
    salutation = models.CharField(max_length=100,choices=Type_of_salutation,default='Mr',null=True)
    firstname = models.CharField(max_length=100,blank=True,null=True)
    lastname = models.CharField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=200,blank=True,null=True)
    address2 = models.CharField(max_length=200,blank=True,null=True)
    city = models.CharField(max_length=100,blank=True,null=True)
    pincode = models.IntegerField(blank=True,null=True)
    alternateaddress = models.CharField(max_length=200,blank=True,null=True)
    alternatemobile = PhoneNumberField(max_length=20,null=True)
    alternateemail = models.EmailField(max_length=100,blank=True,null=True)
    source = models.CharField(max_length=100,null=True,choices=Type_of_Leadsource,default='Advertisement') 
    customertype = models.CharField(max_length=100,choices=Type_of_customer,default='B2B') 
    accounthead = models.CharField(max_length=100,blank=True,null=True)
    tags = models.CharField(max_length=100,null=True,choices=Type_of_Tags,default='All')   
    flyer = models.CharField(max_length=100,blank=True,null=True)
    food = models.CharField(max_length=100,choices=Type_of_food,default="All")
    pan = models.CharField(max_length=30,blank=True,null=True)
    passport = models.CharField(max_length=30,blank=True,null=True)
    enquirydate = models.DateField(auto_now_add=False,blank=True,null=True)
    issuedate = models.DateField(auto_now_add=False,blank=True,null=True)


class supplier(models.Model): 
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_supplier')
    companyname = models.CharField(max_length=255,null=True) 
    aliasname = models.CharField(max_length=255, blank=True,null=True)
    gst = models.IntegerField(null=True, blank=True)
    billingaddress = models.CharField(max_length=255, blank=True,null=True)
    city = models.CharField(max_length=255, blank=True,null=True) 
    deals_in_visa = models.BooleanField(default=False) 
    deals_in_flights = models.BooleanField(default=False)
    deals_in_hotel = models.BooleanField(default=False)
    deals_in_travel_insurance = models.BooleanField(default=False)
    deals_in_forex = models.BooleanField(default=False)
    deals_in_sightseeing = models.BooleanField(default=False)
    deals_in_transport = models.BooleanField(default=False)
    deals_in_cruise = models.BooleanField(default=False)
    deals_in_other = models.BooleanField(default=False)
    deals_in_package = models.BooleanField(default=False)
    deals_in_customize_package = models.BooleanField(default=False)
    deals_in_bus = models.BooleanField(default=False)
    deals_in_train = models.BooleanField(default=False)
    deals_in_passport = models.BooleanField(default=False)
    deals_in_adventure = models.BooleanField(default=False)
    deals_in_group_package = models.BooleanField(default=False)
    country = CountryField(blank_label='(select country)',null=True)
    tags = models.CharField(max_length=100,null=True,choices=Type_of_Tags,default='All') 
    name = models.CharField(max_length=255,null=True,blank=True)
    designation = models.CharField(max_length=255,null=True,blank=True)
    number = PhoneNumberField(max_length=20,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    alternatenumber = PhoneNumberField(max_length=20,null=True,blank=True)
    alternateemail = models.EmailField(null=True,blank=True)
    preffered_supplier = models.BooleanField(default=False)
    inactive_supplier = models.BooleanField(default=False)
    default_email = models.BooleanField(default=False)
    cc_email = models.BooleanField(default=False)
    bankdetails = models.TextField(null=True,blank=True)
    note = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.companyname
    
class Sightseeing(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_sightseen')
    country = CountryField(blank_label='(select country)',null=True)
    city = models.CharField(max_length=255,null=True)
    activity = models.CharField(max_length=255,null=True)
    description = models.TextField(null=True)
    inclusion = models.TextField(null=True)
    exclusion = models.TextField(null=True)
    duration = models.CharField(max_length=255,null=True) 
    closeday = models.CharField(max_length=255,null=True)
    timings = models.CharField(max_length=255,null=True)
    transport = models.CharField(max_length=255,null=True,choices=Type_of_Transport,default='Private')
    time = models.CharField(max_length=255,null=True)
    remark = models.TextField(null=True)
    internalremark = models.TextField(null=True)
    externalremark = models.TextField(null=True)
    image = models.ImageField(upload_to = 'images',null=True, blank=True)

    def __str__(self):
        return self.activity

class Vehicle(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_vehicle')
    country = CountryField(blank_label='(select country)',null=True)
    city = models.CharField(max_length=100,null=True)
    vehicletype = models.CharField(max_length=100,null=True, choices=Type_of_vehicle,default='Select Vehicle Type')
    title = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)
    internalremark = models.TextField(null=True)
    image = models.ImageField(upload_to = 'images',null=True, blank=True)

    def __str__(self):  
        return self.title

class Hotel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_hotel')
    hotelname = models.CharField(max_length=100,blank=True,null=True)
    country = CountryField(blank_label='(select country)',null=True)
    city = models.CharField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    contact = PhoneNumberField(max_length=20,null=True)
    email = models.EmailField(max_length=100,blank=True,null=True)
    rate = models.CharField(max_length=100, choices=[
        ('all','All'),
        ('One Star','One Star'),
        ('Two Star','Two Star'),
        ('Three Star','Three Star'),
        ('Four Star','Four Star'),
        ('Five Star','Five Star')])
    htype = models.CharField(max_length=100, choices=[
        ('All','All'),
        ('Standard','Standard'),
        ('Deluxe','Deluxe'),
        ('Any','Any')])
    childfreeage = models.CharField(max_length=100,blank=True,null=True)
    childwithoutfreeage = models.CharField(max_length=100,blank=True,null=True)
    amenities = models.CharField(max_length=100,blank=True,null=True)
    description = models.CharField(max_length=500,blank=True,null=True)
    image = models.ImageField(upload_to = 'images',null=True)

    def __str__(self):
        # return str(self.hotelname)
        return f'{self.hotelname}--{self.country}'
MEAL_CHOICES = (
        ('AP(Full Board)', 'AP(Full Board)'),
        ('MAP(Half Board)', 'MAP(Half Board)'),
        ('CP(Only Breakfast)', 'CP(Only Breakfast)'),
        ('EP(No Meal)', 'EP(No Meal)'),
        ('Any(Any type of meal)', 'Any(Any type of meal)'),
        ('AI(All Inclusive)', 'AI(All Inclusive)'),
           
    )

class Destination(models.Model):
    destination = models.CharField(max_length=200)
    def __str__(self):
        return str(self.id)


class Package(models.Model): 
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_package')
    packagename = models.CharField(max_length=100,blank=True,null=True)
    country = CountryField(blank=True,null=True)
    # city = models.CharField(max_length=100,blank=True,null=True)
    # stay = models.CharField(max_length=100,blank=True,null=True)
    destinations = models.ManyToManyField(Destination,null=True,blank=True)
    days = models.CharField(max_length=100, choices=Type_of_days,default="1")
    detailed_itenerary = models.TextField(null=True,blank=True)
    tags = models.CharField(max_length=100, choices=Type_of_Tags,default="All")
    overview = models.CharField(max_length=1000,blank=True)
    mealtype = models.CharField(max_length=100, choices=MEAL_CHOICES, default="AI(All Inclusive)")
    hotel_details = models.TextField(max_length=500,blank=True,null=True)
    free_wi_fi = models.BooleanField(default=False)
    airport_transfers_private = models.BooleanField(default=False)
    airport_transfers_sic = models.BooleanField(default=False)
    travel_insurance = models.BooleanField(default=False)
    visa = models.BooleanField(default=False)
    Inter_hotel_transfer_private = models.BooleanField(default=False)
    sightseeing_transfer_private = models.BooleanField(default=False)
    sightseeing_transfer_sic = models.BooleanField(default=False)
    Inter_hotel_transfer_sic = models.BooleanField(default=False)
    candlelight_dinner = models.BooleanField(default=False)
    bed_decorations = models.BooleanField(default=False)
    honeymoon_cake = models.BooleanField(default=False)
    private_ferry = models.BooleanField(default=False)
    private_cruise = models.BooleanField(default=False) 
    scuba_diving = models.BooleanField(default=False)
    parasailing = models.BooleanField(default=False)
    sea_walk = models.BooleanField(default=False)
    photoshoot_for_couple = models.BooleanField(default=False)
    candle_light_dinner_with_wine = models.BooleanField(default=False)
    candle_light_dinner_without_wine = models.BooleanField(default=False)
    jet_ski = models.BooleanField(default=False)
    snorkeling = models.BooleanField(default=False)
    airport_transfers_speed_boat_seaplane = models.BooleanField(default=False)
    image = models.ImageField(upload_to = 'images',null=True,blank=True)
    inclusive = models.TextField(max_length=1000,blank=True,null=True)
    exclusive = models.TextField(max_length=1000,blank=True,null=True)
    created = models.DateTimeField(editable=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True )
    terms_and_conditions = models.TextField(max_length=1000,null=True,blank=True)
    cancellation_policy = models.TextField(max_length=1000,null=True,blank=True)    
    
    def __str__(self) -> str:
        return f'{self.packagename}---{self.country}'
    
class WhatsAppNumber(models.Model):
    number = models.CharField(max_length=20)   
    
    