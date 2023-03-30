# forms.py
from django import forms
from .models import *
from django.forms import modelformset_factory


# class LeadForm(forms.ModelForm):
#     class Meta:
#         model=Lead
#         fields = '__all__'
        
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
