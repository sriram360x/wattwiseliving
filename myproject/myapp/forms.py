from django import forms
from .models import Appliance

class ApplianceForm(forms.ModelForm):
    class Meta:
        model = Appliance
        fields = ['appliances', 'power', 'hours', 'days']
        help_texts = {
            'power': 'Power rating in watts',
            'hours': 'Daily usage in hours',
            'days': 'Days used in a month',
        }
