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
Type_of_Preferencee=(
    ('Private','Private'),
    ('SIC','SIC'),
    ('Self Drive','Self Drive'),
)
Type_of_currency = (
    ('AFN', 'Afghan Afghani'),
    ('ALL', 'Albanian Lek'),
    ('DZD', 'Algerian Dinar'),
    ('AOA', 'Angolan Kwanza'),
    ('ARS', 'Argentine Peso'),
    ('AMD', 'Armenian Dram'),
    ('AWG', 'Aruban Florin'),
    ('AUD', 'Australian Dollar'),
    ('AZN', 'Azerbaijani Manat'),
    ('BSD', 'Bahamian Dollar'),
    ('BHD', 'Bahraini Dinar'),
    ('BDT', 'Bangladeshi Taka'),
    ('BBD', 'Barbadian Dollar'),
    ('BYR', 'Belarusian Ruble'),
    ('BEF', 'Belgian Franc'),
    ('BZD', 'Belize Dollar'),
    ('BMD', 'Bermudan Dollar'),
    ('BTN', 'Bhutanese Ngultrum'),
    ('BTC', 'Bitcoin'),
    ('BOB', 'Bolivian Boliviano'),
    ('BAM', 'Bosnia-Herzegovina Convertible Mark'),
    ('BWP', 'Botswanan Pula'),
    ('BRL', 'Brazilian Real'),
    ('GBP', 'British Pound Sterling'),
    ('BND', 'Brunei Dollar'),
    ('BGN', 'Bulgarian Lev'),
    ('BIF', 'Burundian Franc'),
    ('KHR', 'Cambodian Riel'),
    ('CAD', 'Canadian Dollar'),
    ('CVE', 'Cape Verdean Escudo'),
    ('KYD', 'Cayman Islands Dollar'),
    ('XOF', 'CFA Franc BCEAO'),
    ('XAF', 'CFA Franc BEAC'),
    ('XPF', 'CFP Franc'),
    ('CLP', 'Chilean Peso'),
    ('CNY', 'Chinese Yuan'),
    ('COP', 'Colombian Peso'),
    ('KMF', 'Comorian Franc'),
    ('CDF', 'Congolese Franc'),
    ('CRC', 'Costa Rican Colón'),
    ('HRK', 'Croatian Kuna'),
    ('CUC', 'Cuban Convertible Peso'),
    ('CZK', 'Czech Republic Koruna'),
    ('DKK', 'Danish Krone'),
    ('DJF', 'Djiboutian Franc'),
    ('DOP', 'Dominican Peso'),
    ('XCD', 'East Caribbean Dollar'),
    ('EGP', 'Egyptian Pound'),
    ('ERN', 'Eritrean Nakfa'),
    ('EEK', 'Estonian Kroon'),
    ('ETB', 'Ethiopian Birr'),
    ('EUR', 'Euro'),
    ('FKP', 'Falkland Islands Pound'),
    ('FJD', 'Fijian Dollar'),
    ('GMD', 'Gambian Dalasi'),
    ('GEL', 'Georgian Lari'),
    ('DEM', 'German Mark'),
    ('GHS', 'Ghanaian Cedi'),
    ('GIP', 'Gibraltar Pound'),
    ('GRD', 'Greek Drachma'),
    ('GTQ', 'Guatemalan Quetzal'),
    ('GNF', 'Guinean Franc'),
    ('GYD', 'Guyanaese Dollar'),
    ('HTG', 'Haitian Gourde'),
    ('HNL', 'Honduran Lempira'),
    ('HKD', 'Hong Kong Dollar'),
    ('HUF', 'Hungarian Forint'),
    ('ISK', 'Icelandic Króna'),
    ('INR', 'Indian Rupee'),
    ('IDR', 'Indonesian Rupiah'),
    ('IRR', 'Iranian Rial'),
    ('IQD', 'Iraqi Dinar'),
    ('ILS', 'Israeli New Sheqel'),
    ('ITL', 'Italian Lira'),
    ('JMD', 'Jamaican Dollar'),
    ('JPY', 'Japanese Yen'),
    ('JOD', 'Jordanian Dinar'),
    ('KZT', 'Kazakhstani Tenge'),
    ('KES', 'Kenyan Shilling'),
    ('KWD', 'Kuwaiti Dinar'),
    ('KGS', 'Kyrgystani Som'),
    ('LAK', 'Laotian Kip'),
    ('LVL', 'Latvian Lats'),
    ('LBP', 'Lebanese Pound'),
    ('LSL', 'Lesotho Loti'),
    ('LRD', 'Liberian Dollar'),
    ('LYD', 'Libyan Dinar'),
    ('LTL', 'Lithuanian Litas'),
    ('MOP', 'Macanese Pataca'),
    ('MKD', 'Macedonian Denar'),
    ('MGA', 'Malagasy Ariary'),
    ('MWK', 'Malawian Kwacha'),
    ('MYR', 'Malaysian Ringgit'),
    ('MVR', 'Maldivian Rufiyaa'),
    ('MRO', 'Mauritanian Ouguiya'),
    ('MUR', 'Mauritian Rupee'),
    ('MXN', 'Mexican Peso'),
    ('MDL', 'Moldovan Leu'),
    ('MNT', 'Mongolian Tugrik'),
    ('MAD', 'Moroccan Dirham'),
    ('MZM', 'Mozambican Metical'),
    ('MMK', 'Myanmar Kyat'),
    ('NAD', 'Namibian Dollar'),
    ('NPR', 'Nepalese Rupee'),
    ('ANG', 'Netherlands Antillean Guilder'),
    ('TWD', 'New Taiwan Dollar'),
    ('NZD', 'New Zealand Dollar'),
    ('NIO', 'Nicaraguan Córdoba'),
    ('NGN', 'Nigerian Naira'),
    ('KPW', 'North Korean Won'),
    ('NOK', 'Norwegian Krone'),
    ('OMR', 'Omani Rial'),
    ('PKR', 'Pakistani Rupee'),
    ('PAB', 'Panamanian Balboa'),
    ('PGK', 'Papua New Guinean Kina'),
    ('PYG', 'Paraguayan Guarani'),
    ('PEN', 'Peruvian Nuevo Sol'),
    ('PHP', 'Philippine Peso'),
    ('PLN', 'Polish Złoty'),
    ('USD', 'United States Dollar'),
    ('QAR', 'Qatari Rial'),
    ('RON', 'Romanian Leu'),
    ('RUB', 'Russian Ruble'),
    ('RWF', 'Rwandan Franc'),
    ('SHP', 'Saint Helena Pound'),
    ('SVC', 'Salvadoran Colón'),
    ('WST', 'Samoan Tala'),
    ('SAR', 'Saudi Riyal'),
    ('RSD', 'Serbian Dinar'),
    ('SCR', 'Seychellois Rupee'),
    ('SLL', 'Sierra Leonean Leone'),
    ('SGD', 'Singapore Dollar'),
    ('SKK', 'Slovak Koruna'),
    ('SBD', 'Solomon Islands Dollar'),
    ('SOS', 'Somali Shilling'),
    ('ZAR', 'South African Rand'),
    ('KRW', 'South Korean Won'),
    ('XDR', 'Special Drawing Rights'),
    ('LKR', 'Sri Lankan Rupee'),
    ('SDG', 'Sudanese Pound'),
    ('SRD', 'Surinamese Dollar'),
    ('SZL', 'Swazi Lilangeni'),
    ('SEK', 'Swedish Krona'),
    ('CHF', 'Swiss Franc'),
    ('SYP', 'Syrian Pound'),
    ('STD', 'São Tomé and Príncipe Dobra'),
    ('TJS', 'Tajikistani Somoni'),
    ('TZS', 'Tanzanian Shilling'),
    ('THB', 'Thai Baht'),
    ('TOP', 'Tongan Paʻanga'),
    ('TTD', 'Trinidad and Tobago Dollar'),
    ('TND', 'Tunisian Dinar'),
    ('TRY', 'Turkish Lira'),
    ('TMT', 'Turkmenistani Manat'),
    ('UGX', 'Ugandan Shilling'),
    ('UAH', 'Ukrainian Hryvnia'),
    ('AED', 'United Arab Emirates Dirham'),
    ('UYU', 'Uruguayan Peso'),
    ('UZS', 'Uzbekistan Som'),
    ('VUV', 'Vanuatu Vatu'),
    ('VEF', 'Venezuelan Bolívar'),
    ('VND', 'Vietnamese Dong'),
    ('YER', 'Yemeni Rial'),
    ('ZMW', 'Zambian Kwacha'),
    ('ZWL', 'Zimbabwean Dollar')
)
Type_of_class = (
    ('All','All'),
    ('Economy','Economy'),
    ('Premiun Economy','Premiun Economy'),
    ('Business','Business'),
    ('First Class','First Class')
)
Type_of_flexibility = (
    ('+/-0 Day','+/-0 Day'),
    ('+/-3 Day','+/-3 Day'),
    ('+/-6 Day','+/-6 Day'),
    ('+/-1 Week','+/-1 Week'),
    ('+/-3 Week','+/-3 Week'),
)
Type_of_preference = (
    ('All','All'),
    ('One Stop','One Stop'),
    ('Cheapest','Cheapest'),
    ('Direct','Direct')
)
Type_of_preferences = (
    ('Self Drive','Self Drive'),
    ('Chauffer','Chauffer'),
    ('SIC','SIC')
)
Type_of_room = (
    ('Standard','Standard'),
    ('Deluxe','Deluxe'),
    ('Any','Any')
)  
Type_of_rating = (
    ('One Star','One Star'),
    ('Two Star','Two Star'),
    ('Three Star','Three Star'),
    ('Four Star','Four Star'),
    ('Five Star','Five Star')
) 
Type_of_visa_category = (
    ('Business','Business'),
    ('Tourist','Tourist'),
    ('Student','Student'),
    ('Work','Work'),
    ('Transit','Transit')
)
Type_of_visit= (
    ('Single','Single'),
    ('Double','Double'),
    ('Multiple','Multiple')
)
Type_of_insurance= (
    ('Yes','Yes'),
    ('No','No'),
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
    notes = models.TextField(null=True,blank=True)
    flight_Booking = models.BooleanField(default=False)
    hotel_Booking = models.BooleanField(default=False)
    visa = models.BooleanField(default=False)
    travel_Insurance = models.BooleanField(default=False)
    forex = models.BooleanField(default=False)
    sightseeing = models.BooleanField(default=False)
    transport = models.BooleanField(default=False)
    other = models.BooleanField(default=False)
    package = models.BooleanField(default=False)
    customized_Package = models.BooleanField(default=False)
    bus = models.BooleanField(default=False)
    train = models.BooleanField(default=False)
    passport = models.BooleanField(default=False)
    cruise = models.BooleanField(default=False)
    adventure = models.BooleanField(default=False)
    group = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.leadno)

    
    def save(self, *args, **kwargs):
        if self.leadno =="":
            lead_no = (generate_lead_no())
            
            self.leadno=lead_no
        
        super().save(*args, **kwargs)
    
        
class Flight_booking(models.Model):
    dep_from = models.CharField(max_length=100,null=True,blank=True)
    dep_to = models.CharField(max_length=100,null=True,blank=True)
    departure = models.DateTimeField(null=True,blank=True)
    return_to = models.DateTimeField(null=True,blank=True)
    classes = models.CharField(max_length=100,choices=Type_of_class,default='All',null=True,blank=True) 
    domestic_flight = models.BooleanField(default=False)
    internation_flight = models.BooleanField(default=False)
    flexibility = models.CharField(max_length=100,null=True,blank=True,choices=Type_of_flexibility,default='All') 
    preference = models.CharField(max_length=100,null=True,blank=True,choices=Type_of_preference,default='All')
    
    def __str__(self):
        return str(self.id)
    
class FlightBooking(models.Model):
    leads=models.ForeignKey(Lead,on_delete=models.CASCADE,related_name='flite_lead')
    flight = models.ManyToManyField(Flight_booking)
    
    def __str__(self):
        return str(self.leads)


class Hotel_booking(models.Model):
    
    hcountry = CountryField(blank_label='(select country)',null=True,blank=True)
    hcity = models.CharField(max_length=100,null=True,blank=True)
    checkin = models.DateField(null=True,blank=True)
    checkout = models.DateField(null=True,blank=True)
    roomtype = models.CharField(max_length=100,null=True,blank=True,choices=Type_of_room,default='-') 
    rating = models.CharField(max_length=100,null=True,blank=True,choices=Type_of_rating,default='-')
    nights = models.CharField(max_length=100,null=True,blank=True)
    budget = models.FloatField(null=True,blank=True)
    Hotelname = models.CharField(max_length=100,null=True,blank=True)
    rooms = models.CharField(max_length=100,null=True,blank=True)
    # created = models.DateTimeField(editable=False, auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True, null=True, blank=True )

    def __str__(self):
        return str(self.id)
    
class HotelBooking(models.Model):
    leads=models.ForeignKey(Lead,on_delete=models.CASCADE,related_name='hotel_lead')
    hotel = models.ManyToManyField(Hotel_booking)
    
    def __str__(self):
        return str(self.leads)
    
class Visa_booking(models.Model):
    
    country = CountryField(blank_label='(select country)',null=True,blank=True)
    visa_category= models.CharField(max_length=100,null=True,blank=True,choices=Type_of_visa_category,default='-')
    visit_type = models.CharField(max_length=100,null=True,blank=True,choices=Type_of_visit,default='-') 
    duration = models.CharField(max_length=100,null=True,blank=True)
    traveldate = models.DateField(editable=True, auto_now_add=False,null=True,blank=True)
    job_profile = models.CharField(max_length=100,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    qualification = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    # created = models.DateTimeField(editable=False, auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True, null=True, blank=True )

    def __str__(self):
        return str(self.id)
    
class VisaBooking(models.Model):
    leads=models.ForeignKey(Lead,on_delete=models.CASCADE,related_name='visa_lead')
    visa = models.ManyToManyField(Visa_booking)
    
    def __str__(self):
        return str(self.leads)
    
class Travel_insurance(models.Model):
    
    country = CountryField(blank_label='(select country)',null=True,blank=True)
    how_long = models.CharField(max_length=100,null=True,blank=True)
    travel_date = models.DateField(null=True,blank=True)
    insurace = models.CharField(max_length=100,null=True,blank=True,choices=Type_of_insurance,default='-') 
    # created = models.DateTimeField(editable=False, auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True, null=True, blank=True )

    def __str__(self):
        return str(self.id)
    
class TravelInsurance(models.Model):
    leads=models.ForeignKey(Lead,on_delete=models.CASCADE,related_name='travel_insurance_lead')
    travelinsurance = models.ManyToManyField(Travel_insurance)
    
    def __str__(self):
        return str(self.leads)
    
class Forex(models.Model):
    
    currency = models.CharField(max_length=100,choices=Type_of_currency,default='INR',null=True)
    amount = models.IntegerField(null=True,blank=True)
    # created = models.DateTimeField(editable=False, auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True, null=True, blank=True )

    def __str__(self):
        return str(self.id)
    
class LeadForex(models.Model):
    leads=models.ForeignKey(Lead,on_delete=models.CASCADE,related_name='forex_lead')
    forex = models.ManyToManyField(Forex)
    
    def __str__(self):
        return str(self.leads)

class Sightseen(models.Model):
    
    country = CountryField(blank_label='(select country)',null=True,blank=True)
    city = models.CharField(max_length=30,null=True,blank=True)
    sightseen_options = models.CharField(max_length=300,null=True,blank=True)
    preference = models.CharField(max_length=100,choices=Type_of_Transport,default='-',null=True)
    travel_date = models.DateField(null=True,blank=True)
    # created = models.DateTimeField(editable=False, auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True, null=True, blank=True )

    def __str__(self):
        return str(self.id)
    
class LeadSightseen(models.Model):
    leads=models.ForeignKey(Lead,on_delete=models.CASCADE,related_name='sightseen_lead')
    sightseen = models.ManyToManyField(Sightseen)
    
    def __str__(self):
        return str(self.leads)

class Transport(models.Model):
    
    country = CountryField(blank_label='(select country)',null=True,blank=True)
    city = models.CharField(max_length=30,null=True,blank=True)
    trasport_date = models.DateField(null=True,blank=True)
    drop_date = models.DateField(null=True,blank=True)
    preference = models.CharField(max_length=100,choices=Type_of_preferences,default='-',null=True)
    Airport_transfers = models.BooleanField(default=False)
    Sightseeing_transfers = models.BooleanField(default=False)
    Others = models.BooleanField(default=False)
    # created = models.DateTimeField(editable=False, auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True, null=True, blank=True )

    def __str__(self):
        return str(self.id)
    
class LeadTransport(models.Model):
    leads=models.ForeignKey(Lead,on_delete=models.CASCADE,related_name='transport_lead')
    transport = models.ManyToManyField(Transport)
    
    def __str__(self):
        return str(self.leads)

class Other(models.Model):
    
    country = CountryField(blank_label='(select country)',null=True,blank=True)
    travel_date = models.DateField(null=True,blank=True)
    no_of_days = models.IntegerField(null=True,blank=True)
    sub_category = models.CharField(max_length=30,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    # created = models.DateTimeField(editable=False, auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True, null=True, blank=True )

    def __str__(self):
        return str(self.id)
    
class LeadOther(models.Model):
    leads=models.ForeignKey(Lead,on_delete=models.CASCADE,related_name='other_lead')
    other = models.ManyToManyField(Other)
    
    def __str__(self):
        return str(self.leads)

class Packagee(models.Model):
    
    travel_date = models.DateField(null=True,blank=True)
    budget = models.IntegerField(null=True,blank=True)
    country = CountryField(blank_label='(select country)',null=True,blank=True)
    package_name = models.CharField(max_length=30,null=True,blank=True)
    extra_details = models.TextField(null=True,blank=True)
    # created = models.DateTimeField(editable=False, auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True, null=True, blank=True )

    def __str__(self):
        return str(self.id)
    
class LeadPackage(models.Model):
    leads=models.ForeignKey(Lead,on_delete=models.CASCADE,related_name='package_lead')
    package = models.ManyToManyField(Packagee)
    
    def __str__(self):
        return str(self.leads)
    
class Customized_Package(models.Model):
    
    country = CountryField(blank_label='(select country)',null=True,blank=True)
    service = models.CharField(max_length=30,null=True,blank=True)
    rating = models.CharField(max_length=100,choices=Type_of_rating,default='-',null=True)
    travel_date = models.DateField(null=True,blank=True)
    no_of_night = models.IntegerField(null=True,blank=True)
    flexibility = models.CharField(max_length=100,choices=Type_of_flexibility,default='-',null=True)
    no_of_rooms = models.IntegerField(null=True,blank=True)
    preferance = models.CharField(max_length=100,choices=Type_of_Preferencee,default='-',null=True)
    budget = models.IntegerField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    # created = models.DateTimeField(editable=False, auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True, null=True, blank=True )

    def __str__(self):
        return str(self.id)
    
class CustomizedPackage(models.Model):
    leads=models.ForeignKey(Lead,on_delete=models.CASCADE,related_name='customized_package_lead')
    customizedpackage = models.ManyToManyField(Customized_Package)
    
    def __str__(self):
        return str(self.leads)

class Bus(models.Model):
    
    country = CountryField(blank_label='(select country)',null=True,blank=True)
    From = models.CharField(max_length=30,null=True,blank=True)
    to = models.CharField(max_length=30,null=True,blank=True)
    departure = models.DateField(null=True,blank=True)
    Return = models.DateField(null=True,blank=True)
    preference = models.CharField(max_length=100,choices=Type_of_Transport,default='-',null=True)
    remark = models.TextField(null=True,blank=True)
    # created = models.DateTimeField(editable=False, auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True, null=True, blank=True )

    def __str__(self):
        return str(self.id)
    
class LeadBus(models.Model):
    leads=models.ForeignKey(Lead,on_delete=models.CASCADE,related_name='bus_lead')
    bus = models.ManyToManyField(Bus)
    
    def __str__(self):
        return str(self.leads)
    
class Train(models.Model):
    
    country = CountryField(blank_label='(select country)',null=True,blank=True)
    From = models.CharField(max_length=30,null=True,blank=True)
    to = models.CharField(max_length=30,null=True,blank=True)
    departure = models.DateField(null=True,blank=True)
    Return = models.DateField(null=True,blank=True)
    preference = models.CharField(max_length=100,choices=Type_of_Transport,default='-',null=True)
    remark = models.TextField(null=True,blank=True)
    # created = models.DateTimeField(editable=False, auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True, null=True, blank=True )

    def __str__(self):
        return str(self.id)
    
class LeadTrain(models.Model):
    leads=models.ForeignKey(Lead,on_delete=models.CASCADE,related_name='train_lead')
    train = models.ManyToManyField(Train)
    
    def __str__(self):
        return str(self.leads)
    
class Passport(models.Model):
    country = CountryField(blank_label='(select country)',null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    passport_no = models.CharField(max_length=30,null=True,blank=True)
    place_of_apply = models.CharField(max_length=30,null=True,blank=True)
    no_of_person = models.IntegerField(null=True,blank=True)
    new_passport = models.BooleanField(default=False)
    renew_passport = models.BooleanField(default=False)
    urgent = models.BooleanField(default=False)
    remark = models.TextField(null=True,blank=True)
    # created = models.DateTimeField(editable=False, auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True, null=True, blank=True )

    def __str__(self):
        return str(self.id)
    
class LeadPassport(models.Model):
    leads=models.ForeignKey(Lead,on_delete=models.CASCADE,related_name='passport_lead')
    passport = models.ManyToManyField(Passport)
    
    def __str__(self):
        return str(self.leads)

class Cruise(models.Model):
    
    country = CountryField(blank_label='(select country)',null=True,blank=True)
    City = models.CharField(max_length=30,null=True,blank=True)
    days = models.IntegerField(null=True,blank=True)
    Cruise_name = models.CharField(max_length=30,null=True,blank=True)
    type = models.CharField(max_length=30,null=True,blank=True) 
    departure = models.DateField(null=True,blank=True)
    Return = models.DateField(null=True,blank=True)
    room_type = models.CharField(max_length=100,choices=Type_of_Preferencee,default='-',null=True)
    remark = models.TextField(null=True,blank=True)
    # created = models.DateTimeField(editable=False, auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True, null=True, blank=True )

    def __str__(self):
        return str(self.id)
    
class LeadCruise(models.Model):
    leads=models.ForeignKey(Lead,on_delete=models.CASCADE,related_name='cruise_lead')
    cruise = models.ManyToManyField(Cruise)
    
    def __str__(self):
        return str(self.leads)
    
class Adventure(models.Model):
    
    country = CountryField(blank_label='(select country)',null=True,blank=True)
    city = models.CharField(max_length=30,null=True,blank=True)
    travel_date = models.DateField(null=True,blank=True)
    motorbiking = models.BooleanField(default=False)
    camping = models.BooleanField(default=False)
    safari = models.BooleanField(default=False)
    water_sports = models.BooleanField(default=False)
    remark = models.TextField(null=True,blank=True)
    # created = models.DateTimeField(editable=False, auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True, null=True, blank=True )

    def __str__(self):
        return str(self.id)
    
class LeadAdventure(models.Model):
    leads=models.ForeignKey(Lead,on_delete=models.CASCADE,related_name='adventure_lead')
    adventure = models.ManyToManyField(Adventure)
    
    def __str__(self):
        return str(self.leads)
    
class Group(models.Model):
    
    country = CountryField(blank_label='(select country)',null=True,blank=True)
    package_name = models.CharField(max_length=30,null=True,blank=True)
    preference = models.CharField(max_length=100,choices=Type_of_preferences,default='-',null=True)
    remark = models.TextField(null=True,blank=True)
    # created = models.DateTimeField(editable=False, auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True, null=True, blank=True )

    def __str__(self):
        return str(self.id)
    
class LeadGroup(models.Model):
    leads=models.ForeignKey(Lead,on_delete=models.CASCADE,related_name='group_lead')
    group = models.ManyToManyField(Group)
    
    def __str__(self):
        return str(self.leads)

class customer(models.Model): 
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_customer')
    number = models.CharField(max_length=20,null=True)
    email = models.EmailField(max_length=100,blank=True,null=True)
    salutation = models.CharField(max_length=100,choices=Type_of_salutation,default='Mr',null=True)
    firstname = models.CharField(max_length=100,blank=True,null=True)
    lastname = models.CharField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=200,blank=True,null=True)
    address2 = models.CharField(max_length=200,blank=True,null=True)
    city = models.CharField(max_length=100,blank=True,null=True)
    pincode = models.IntegerField(blank=True,null=True)
    alternateaddress = models.CharField(max_length=200,blank=True,null=True)
    alternatemobile = models.CharField(max_length=20,null=True,blank=True)
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
    company_name = models.CharField(max_length=255,null=True) 
    alias_name = models.CharField(max_length=255, blank=True,null=True)
    gst_no = models.CharField(max_length=20,null=True, blank=True)
    billing_address = models.CharField(max_length=255, blank=True,null=True)
    city = models.CharField(max_length=255, blank=True,null=True) 
    visa = models.BooleanField(default=False) 
    flights = models.BooleanField(default=False)
    hotel = models.BooleanField(default=False)
    travel_insurance = models.BooleanField(default=False)
    forex = models.BooleanField(default=False)
    sightseeing = models.BooleanField(default=False)
    transport = models.BooleanField(default=False)
    cruise = models.BooleanField(default=False)
    other = models.BooleanField(default=False)
    package = models.BooleanField(default=False)
    customize_package = models.BooleanField(default=False)
    bus = models.BooleanField(default=False)
    train = models.BooleanField(default=False)
    passport = models.BooleanField(default=False)
    adventure = models.BooleanField(default=False)
    group_package = models.BooleanField(default=False)
    country = CountryField(blank_label='(select country)',null=True)
    tags = models.CharField(max_length=100,null=True,choices=Type_of_Tags,default='All') 
    name = models.CharField(max_length=255,null=True,blank=True)
    designation = models.CharField(max_length=255,null=True,blank=True)
    number = models.CharField(max_length=20,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    alternate_number = models.CharField(max_length=20,null=True,blank=True)
    alternate_email = models.EmailField(null=True,blank=True)
    preffered_supplier = models.BooleanField(default=False)
    inactive_supplier = models.BooleanField(default=False)
    default_email = models.BooleanField(default=False)
    cc_email = models.BooleanField(default=False)
    bank_details = models.TextField(null=True,blank=True)
    note = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.company_name
    
class Sightseeing(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_sightseen')
    country = CountryField(blank_label='(select country)',null=True)
    city = models.CharField(max_length=255,null=True)
    activity = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    inclusion = models.TextField(null=True,blank=True)
    exclusion = models.TextField(null=True,blank=True)
    duration = models.CharField(max_length=255,null=True,blank=True) 
    close_day = models.CharField(max_length=255,null=True,blank=True)
    timings = models.CharField(max_length=255,null=True,blank=True)
    transport = models.CharField(max_length=255,null=True,choices=Type_of_Transport,default='Private')
    time = models.CharField(max_length=255,null=True,blank=True)
    remark = models.TextField(null=True,blank=True)
    internal_remark = models.TextField(null=True,blank=True)
    external_remark = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to = 'images',null=True, blank=True)

    def __str__(self):
        return self.activity

class Vehicle(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_vehicle')
    country = CountryField(blank_label='(select country)',null=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    vehicle_type = models.CharField(max_length=100,null=True, choices=Type_of_vehicle,default='Select Vehicle Type')
    title = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    internal_remark = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to = 'images',null=True, blank=True)

    def __str__(self):  
        return self.title

class Hotel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_hotel')
    hotel_name = models.CharField(max_length=100,blank=True,null=True)
    country = CountryField(blank_label='(select country)',null=True)
    city = models.CharField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    contact = models.CharField(max_length=20,null=True)
    email = models.EmailField(max_length=100,blank=True,null=True)
    rate = models.CharField(max_length=100, choices=[
        ('all','All'),
        ('One Star','One Star'),
        ('Two Star','Two Star'),
        ('Three Star','Three Star'),
        ('Four Star','Four Star'),
        ('Five Star','Five Star')])
    hotel_type = models.CharField(max_length=100, choices=[
        ('All','All'),
        ('Standard','Standard'),
        ('Deluxe','Deluxe'),
        ('Any','Any')])
    child_freeage = models.CharField(max_length=100,blank=True,null=True)
    child_without_freeage = models.CharField(max_length=100,blank=True,null=True)
    amenities = models.CharField(max_length=100,blank=True,null=True)
    description = models.CharField(max_length=500,blank=True,null=True)
    image = models.ImageField(upload_to = 'images',null=True,blank=True)
    
    def __str__(self):
        # return str(self.hotelname)
        return f'{self.hotel_name}--{self.country}'
    
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
    package_name = models.CharField(max_length=100,blank=True,null=True)
    country = CountryField(blank=True,null=True)
    # city = models.CharField(max_length=100,blank=True,null=True)
    # stay = models.CharField(max_length=100,blank=True,null=True)
    destinations = models.ManyToManyField(Destination,null=True,blank=True)
    days = models.CharField(max_length=100, choices=Type_of_days,default="1")
    detailed_itenerary = models.TextField(null=True,blank=True)
    tags = models.CharField(max_length=100, choices=Type_of_Tags,default="All")
    overview = models.CharField(max_length=1000,blank=True)
    meal_type = models.CharField(max_length=100, choices=MEAL_CHOICES, default="AI(All Inclusive)")
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
        return f'{self.package_name}---{self.country}'
    
class WhatsAppNumber(models.Model):
    number = models.CharField(max_length=20)   
    
    