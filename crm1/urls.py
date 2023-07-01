
from django.contrib import admin
from django.urls import path,include
from main import views
from Useraccount.views import RegisterView,LoginView ,UserDeleteView
urlpatterns = [
    path("admin/", admin.site.urls),
    # path("",views.home),
    path('accounts/', include('allauth.urls')),
    path("",views.maincontent,name="maincontent"),
    path("about/",views.about ,name="about"), 
    path("features/",views.features ,name="features"),
    path("calendy/",views.calendy,name="calendy"),
    path("clients/",views.clients,name="clients"),
    path("contactus/",views.contactus,name="contactus"),
    path("pricing/",views.pricing,name="pricing"),
    path("privacypolicy/",views.privacypolicy,name="privacypolicy"),
    path("termsandconditions/",views.termsandconditions,name="termsandconditions"),
    
    path("dashboard/",views.dashboard,name="dashboard"),
    
    path("leads/",views.leads,name="leads"),
    path("addleads/",views.LeadAddView.as_view(),name="addleads"),
    path("editleads/<int:pk>",views.LeadUpdateView.as_view(),name="editleads"),
    path('delete/<int:id>', views.delete, name='delete'),
    path('viewlead/<int:id>', views.viewlead, name='viewlead'),
    
    path("Flightbooking/",views.AddFlightBooking,name="Flightbooking"),
    path('display-flight-bookings/', views.displayflightbooking, name='display_flight_bookings'),
    path("HotelBooking/",views.AddHotelBooking,name="HotelBooking"),
    path('display-hotel-bookings/', views.displayhotelbooking, name='display_hotel_bookings'),
    path("VisaBooking/",views.AddVisaBooking,name="VisaBooking"),
    path('display-visa-bookings/', views.displayvisa, name='display_visa_bookings'),
    path("TravelInsurance/",views.AddTravelInsurance,name="TravelInsurance"),
    path('display-travelinsurance-bookings/', views.displaytravelinsurance, name='display_travelinsurance_bookings'),
    path("Forex/",views.AddForex,name="Forex"),
    path('display-forex-bookings/', views.displayforex, name='display_forex_bookings'),
    path("Sightseen/",views.AddSightseen,name="Sightseen"),
    path('display-sightseen-bookings/', views.displaysightseen, name='display_sightseen_bookings'),
    path("Travel/",views.AddTravel,name="Travel"),
    path('display-travel-bookings/', views.displaytravel, name='display_travel_bookings'),
    path("Other/",views.AddOther,name="Other"),
    path('display-other-bookings/', views.displayother, name='display_other_bookings'),
    path("Packagee/",views.AddPackagee,name="Packagee"),
    path('display-package-bookings/', views.displaypackage, name='display_package_bookings'),
    path("CustomizedPackage/",views.AddCustomizedPackage,name="CustomizedPackage"),
    path('display-customizedpackage-bookings/', views.displaycustomizedpackage, name='display_customizedpackage_bookings'),
    path("Bus/",views.AddBus,name="Bus"),
    path('display-bus-bookings/', views.displaybus, name='display_bus_bookings'),
    path("Train/",views.AddTrain,name="Train"),
    path('display-Train-bookings/', views.displayTrain, name='display_Train_bookings'),
    path("Passport/",views.AddPassport,name="Passport"),
    path('display-Passport-bookings/', views.displayPassport, name='display_Passport_bookings'),
    path("Cruise/",views.AddCruise,name="Cruise"),
    path('display-Cruise-bookings/', views.displayCruise, name='display_Cruise_bookings'),
    path("Adventure/",views.AddAdventure,name="Adventure"),
    path('display-Adventure-bookings/', views.displayAdventure, name='display_Adventure_bookings'),
    path("Group/",views.AddGroup,name="Group"),
    path('display-group-bookings/', views.displaygroup, name='display_group_bookings'),
    
    
    path('user/', views.people, name='user'),
    path('adduser/', views.AdduserView.as_view(), name='adduser'),
    path("edituser/<int:id>",views.edituser,name="edituser"),
    path('viewuser/<int:id>', views.viewUser, name='viewuser'),
    
    path("customer/",views.contact,name="customer"), 
    path("addcustomer/",views.CustomerAddView.as_view(),name="addcustomer"),
    path("editcustomer/<int:pk>",views.CustomerUpdateView.as_view(),name="editcustomer"),
    path('viewcustomer/<int:id>', views.viewcustomer, name='viewcustomer'),
    
    path("supplier/",views.Supplier,name="supplier"),
    path("addsupplier/",views.SupplierAddView.as_view(),name="addsupplier"),
    path("editsupplier/<int:pk>",views.SupplierUpdateView.as_view(),name="editsupplier"),
    path('viewsupplier/<int:id>', views.viewsupplier, name='viewsupplier'),
    
    path("signup/",RegisterView.as_view(),name="signup"),
    path("login/",LoginView.as_view(),name="login"),
    path("logout/",views.logoutPage,name="logout"),
    
    path("sightseeing/",views.sightseeing,name="sightseeing"),
    path("addsightseeing/",views.SightseeingAddView.as_view(),name="addsightseeing"),
    path("editsightseeing/<int:pk>",views.SightseeingUpdateView.as_view(),name="editsightseeing"),
    path('viewsightseeing/<int:id>', views.viewsightseeing, name='viewsightseeing'),
    
    path("transport/",views.transport,name="transport"),
    path ('addtransport',views.TransportAddView.as_view(),name="addtransport"),
    path("edittransport/<int:pk>",views.TransportUpdateView.as_view(),name="edittransport"),
    path('viewtransport/<int:id>', views.viewtransport, name='viewtransport'),
    
    path("visainfo/",views.visa,name="visa"),
    path("addvisa/",views.addvisa,name="addvisa"),
    
    path('viewprofile/<int:id>', views.viewProfile, name='viewprofile'),
    
    path("hotels/",views.hotels, name="hotels"),
    # path("addhotels/",views.addhotels, name="addhotels"),
    path ('addhotels',views.HotelAddView.as_view(),name="addhotels"),
    path("viewhotels/<int:id>",views.viewhotels,name="viewhotels"),
    path("edithotels/<int:pk>",views.HotelUpdateView.as_view(),name="edithotels"),
    
    path("packages/",views.packages, name="packages"),
    path("addpackages/",views.addpackages, name="addpackages"),
    path('viewpackages/<int:id>',views.viewpackages, name='viewpackages'),
    # path('editpackages/<int:id>',views.editpackages, name='editpackages'),
    path('generateinvoice/<int:id>', views.GenerateInvoice.as_view(), name = 'generateinvoice'),
    path("editpackages/<int:pk>", views.PackageUpdateView.as_view(), name="editpackages"),
    path("add/", views.BirdAddView.as_view(), name="add_bird"),

    # api urls 

    path("leadapi/",views.lead_api),
    path("leadapi/<int:pk>", views.lead_api),
    path("customerapi/", views.customer_api),
    path("customerapi/<int:pk>", views.customer_api),
    path("supplierapi/", views.supplier_api),
    path("supplierapi/<int:pk>", views.supplier_api),
    path("sightseeingapi/", views.sightseeing_api),
    path("sightseeingapi/<int:pk>", views.sightseeing_api),
    path("packageapi/", views.package_api),
    path("packageapi/<int:pk>", views.package_api),
    path("vehicleapi/", views.vehicle_api),
    path("vehicleapi/<int:pk>", views.vehicle_api),
    path("hotelapi/", views.hotel_api),
    path("hotelapi/<int:pk>", views.hotel_api),
    path("userapi/", views.user_api),
    path("userapi/<int:pk>", views.user_api),
    
    
]
