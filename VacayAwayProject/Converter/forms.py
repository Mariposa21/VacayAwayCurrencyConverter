from django import forms
from .models import *

class VacationForm(forms.ModelForm):
    class Meta:
        model = vacation
        fields = ['countryOrigin', 'countryArrival', 'vacationId']
        CURRENCY_OPTIONS = [("USD", "United States"), ("EUR","Italy"), 
                        ("EUR","Spain"), ("MXN","Mexico"), 
                        ("CAN","Canada")]
        countryOrigin = forms.CharField(
            widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'display' : 'inline'
            }))
        countryArrival = forms.CharField(
            widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'style': 'max-width: 300px;'
            }))
        labels = {
            'countryOrigin' : 'Country of Departure', 
            'countryArrival' : 'Country of Arrival'
        }

class CostCategoryForm(forms.ModelForm): 
  class Meta: 
       model = costCategory
       fields = ['costCategory', 'originCostAmount', 'arrivalCostAmount', 'vacation']
       costCategory = forms.CharField(
            widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'label': 'costCategory', 
                'display': 'inline'
            }))
       originCostAmount = forms.CharField(
            widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'label': 'originCostAmount'
            }))
  def populateFormRow(self, costCategory):
        self.fields['costCategory'].initial = costCategory
        self.fields['costCategory'].widget = forms.HiddenInput()
        self.fields['vacation'].widget = forms.HiddenInput()
        self.fields['arrivalCostAmount'].widget = forms.HiddenInput()
        return self 
      
