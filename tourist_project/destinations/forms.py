from django import forms
from .models import Destination

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['place_name', 'weather', 'state', 'district', 'google_map_link', 'image', 'description']