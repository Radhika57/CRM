from django.contrib import admin
from .models import *
    
class LeadAdmin(admin.ModelAdmin):
    list_display = ['leadno','customertype','number','email','salutation','firstname','lastname','address','city','alternatenumber','alternateemail','leadsource','priority','status','adults','child','infants','tags','triptype','assigned']
    
class customerAdmin(admin.ModelAdmin):
    list_display = ['number','email','salutation','firstname','lastname','address','address2','city','pincode','alternateaddress','alternatemobile','alternateemail','source','customertype','accounthead','tags','flyer','food','pan','passport','enquirydate','issuedate']

class supplierAdmin(admin.ModelAdmin):
    list_display=['companyname','aliasname','name','number','email']
   
class sightseeingAdmin(admin.ModelAdmin):
    list_display=['country','city','activity','duration','image'] 
    
class VehicleAdmin(admin.ModelAdmin):
    list_display=['country','city','vehicletype'] 
    
class HotelAdmin(admin.ModelAdmin):
    list_display = ['hotelname','country','city','address','contact','email','rate','htype','childfreeage','childwithoutfreeage','amenities','description','image']

class DestinationAdmin(admin.ModelAdmin):
    list_display=['destination'] 
    
    
class PackageAdmin(admin.ModelAdmin):
    raw_id_fields = ['destinations']
    list_display = ['packagename','country','tags','overview','mealtype','image','inclusive','exclusive']

class WhatsappAdmin(admin.ModelAdmin):
    list_display = ['number']

admin.site.register(Lead,LeadAdmin)
admin.site.register(customer,customerAdmin)
admin.site.register(supplier,supplierAdmin)
admin.site.register(Sightseeing,sightseeingAdmin)
admin.site.register(Vehicle,VehicleAdmin)
admin.site.register(Hotel,HotelAdmin)
admin.site.register(Package,PackageAdmin)
admin.site.register(Destination,DestinationAdmin)
admin.site.register(WhatsAppNumber,WhatsappAdmin)






# from django.contrib import admin
# from django.urls import reverse
# from django.utils.html import format_html
# from django.contrib.auth.models import User
# from Useraccount.models import User

# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'is_staff', 'is_active', 'block_user_link')

#     def block_user_link(self, obj):
#         if obj.is_active:
#             url = reverse('admin:block_user', args=[obj.id])
#             return format_html('<a href="{}">Block user</a>', url)
#         else:
#             return format_html('<span style="color: #ccc">Blocked</span>')

#     block_user_link.short_description = 'Block user'

# admin.site.register(User, UserAdmin)
# admin.site.unregister(User)




